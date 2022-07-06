from xml_helper import *
from sax_parser import *
import requests as re
import xml.etree.ElementTree as ET
import subprocess
import os
import pathlib
import sys
import psutil
import signal
import time


def call(query, type):
    query_server = "http://localhost:9999/blazegraph/namespace/kb/sparql"
    #print("Sending Query")
    response = re.get(query_server, params={"query": query})
    #print("Response recieved")

    unwanted_text = "xmlns='http://www.w3.org/2005/sparql-results#'"
    xmlstr = response.text.replace(unwanted_text, "")

    resdata = ET.fromstring(xmlstr)
    solutions = []
    for result in resdata.findall("results/result"):
        if type == "top-3-keywords":
            keyword = result.find("binding/uri").text
            count = result.find("binding/literal").text
            solutions.append((keyword, count))
        else:
            value = result.find("binding/uri").text
            solutions.append(value)

    return solutions


def coauth(problem):
    query = """
    PREFIX info: <https://zbmath.org/infos#>
    SELECT DISTINCT ?author
    WHERE
    {
        VALUES ?coauthor { <""" + problem.queries[0] + """> }
        ?record info:author ?coauthor.
        ?record info:author ?author.
        FILTER(?author != ?coauthor).
    }
    """
    #print(problem.queries)
    if problem.withquery:
        problem.query = query

    problem.solutions = call(query, problem.type)

    return problem


def msc_inter(problem):
    classification = ""

    # add triples
    for i in range(len(problem.queries)):
        class_ = "?record  info:classification ?class" + str(i+1) + ".\n"
        classification += class_

    # add filters
    for i in range(len(problem.queries)):
        filter = f"FILTER(regex(str(?class{i+1}), \"{problem.queries[i][38:]}\")).\n"
        classification += filter

    query = """
    PREFIX info: <https://zbmath.org/infos#>
    SELECT ?record
    WHERE{
    
    """
    query += classification
    query += "\n"
    query += "}"

    if problem.withquery:
        problem.query = query

    problem.solutions = call(query, problem.type)

    return problem


def top3(problem):

    before = f"?year < \"{problem.before}\"" if problem.before else ""
    after = f"?year > \"{problem.after}\"" if problem.after else ""

    year_filter = " "
    if before != "" and after != "":
        year_filter = f"FILTER({before} && {after})"
    elif before != "" and after == "":
        year_filter = f"FILTER({before})"
    elif before == "" and after != "":
        year_filter = f"FILTER({after})"

    query = """
    PREFIX info: <https://zbmath.org/infos#>
    SELECT ?keyword (count(distinct ?record) AS ?count)
    WHERE
    {
      ?record info:author <""" + problem.queries[0] + """>.
      ?record info:year ?year.
      ?record info:keyword ?keyword.
      """ + year_filter + """
    }
    GROUP BY ?keyword
    ORDER BY desc(?count)
    LIMIT 3
    """

    if problem.withquery:
        problem.query = query

    problem.solutions = call(query, problem.type)

    return problem


def papersearch(auth1, auth2):
    query = """
        PREFIX info: <https://zbmath.org/infos#>
        SELECT ?record
        WHERE
        {
            ?record info:author <""" + auth1 + """>.
            ?record info:author <""" + auth2 + """>.
        }
        """

    solutions = call(query, "paperserach")

    return solutions


def coaudis(problem):
    'Return minimal connection between 2 authors'
    'Connection is over authors and their work'

    'Return connecting authors and papers'
    'Save path with every search'

    found = False

    a1 = problem.frm
    a2 = problem.to

    o1 = Coauth(a1)
    o2 = Coauth(a2)

    'Current Coauthor list'
    coauth1 = []
    coauth2 = []

    'Search space'
    search1 = {a1: o1}
    search2 = {a2: o2}
    #print(search1)
    nextsearch1 = {}
    nextsearch2 = {}

    'Already visited coauthors'
    visited1 = set()
    visited2 = set()

    foundin = 0

    work = None
    start = None

    nextpaper = None

    i = 0

    while(not found):

        if not found:
            i += 1

            for c in search1:
                coauthsearch1 = Problem(0, "coauthor", False, [c], None, None, None, None)
                coauth1 = coauth(coauthsearch1)
                visited1.add(c)
                for coa in coauth1.solutions:
                    if coa not in visited1:
                        paper = papersearch(c, coa)[0]
                        nextsearch1[coa] = Coauth(coa)
                        nextsearch1[coa].prev = search1[c]
                        nextsearch1[coa].paper = paper
                        if coa in search2:
                            found = True
                            foundin = 1
                            nextsearch1[coa].next = search2[coa].next
                            if nextsearch1[coa].next is not None:
                                nextsearch1[coa].next.prev = nextsearch1[coa]
                            nextsearch1[coa].paper = search2[coa].paper
                            nextpaper = paper
                            work = nextsearch1[coa]
                            break
                if found:
                    break

            if not found:
                for c in search2:
                    coauthsearch2 = Problem(0, "coauthor", False, [c], None, None, None, None)
                    coauth2 = coauth(coauthsearch2)
                    visited2.add(c)
                    for coa in coauth2.solutions:
                        if coa not in visited2:
                            paper = papersearch(c, coa)[0]
                            nextsearch2[coa] = Coauth(coa)
                            nextsearch2[coa].next = search2[c]
                            nextsearch2[coa].paper = paper
                            if coa in search1:
                                found = True
                                foundin = 2
                                nextsearch2[coa].prev = search1[coa].prev
                                if nextsearch2[coa].prev is not None:
                                    nextsearch2[coa].prev.next = nextsearch2[coa]
                                nextpaper = nextsearch2[coa].paper
                                nextsearch2[coa].paper = search1[coa].paper
                                work = nextsearch2[coa]
                                break
                    if found:
                        break

                search1.clear()
                for c in nextsearch1:
                    search1[c] = nextsearch1[c]
                nextsearch1.clear()

                search2.clear()
                for c in nextsearch2:
                    search2[c] = nextsearch2[c]
                nextsearch2.clear()

    left = None
    right = None

    if foundin == 1:
        left = work
        right = work.next
    elif foundin == 2:
        left = work.prev
        right = work

    if right is not None:
        while right.next is not None:
            right.next.prev = right
            right = right.next
    if left is not None:
        while left.prev is not None:
            paperbuff = left.prev.paper
            left.prev.paper = nextpaper
            nextpaper = paperbuff
            left.prev.next = left
            left = left.prev
    start = left

    while start.next is not None:
        problem.solutions.append(start)
        start = start.next
    problem.solutions.append(start)

    return problem


def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def findProcessIdByName(processName):
    '''
    Get a list of all the PIDs of a all the running process whose name contains
    the given string processName
    '''

    listOfProcessObjects = []

    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
            # Check if process name contains the given name string.
            if processName.lower() in pinfo['name'].lower():
                listOfProcessObjects.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listOfProcessObjects


def dbinit(file):
    # if not running then run server first
    if not checkIfProcessRunning("java"):
        process = subprocess.Popen(['java', '-jar', 'blazegraph.jar'], stdout=subprocess.PIPE)
        # now wait for 2 min for server starting
        print(f"wait 30 secs for server starting...")
        time.sleep(30)



    # update the db with rdf data
    query_server = "http://localhost:9999/blazegraph/namespace/kb/sparql"
    abs_file_path = pathlib.Path(file).absolute()
    query = f"LOAD <file:///{abs_file_path}>"
    response = re.post(query_server, params={"update": query})
    print("Graph updated!")


def dbterminate():
    if checkIfProcessRunning("java"):
        infos = findProcessIdByName("java")
        for info in infos:
            os.kill(info['pid'], signal.SIGKILL)


def run(problem_file):
    # load problem file
    problems = xml_read(problem_file)

    # get the query result by problem type
    for problem in problems:
        if problem.type == "coauthors":
            problem = coauth(problem)

        elif problem.type == "msc-intersection":
            problem = msc_inter(problem)

        elif problem.type == "top-3-keywords":
            problem = top3(problem)

        elif problem.type == "coauth-dist":
            problem = coaudis(problem)

    # write solutions to solution.xml
    xml_write(problems)


def isTypeExists(args, extension: str):
    for i in range(1, len(args)):
        if args[i].endswith(extension):
            return True
    return False

def systemize():
    args = sys.argv

    # -b build rdfdata.rdf and logics
    if args[1] == "-b" and args[2].endswith("xml"):
        xmlfile = args[2]
        # convert xml to rdf data
        buildRdfDataFile(xmlfile)
        print("`rdfdata.rdf` is created successfully!")

    # -w write date to blazegraph with others
    if args[1] == "-b" and args[3] == "-w":
        dbinit("rdfdata.rdf")
    elif args[1] == "-w" and args[2].endswith("rdf"):
        rdffile = args[2]
        dbinit(rdffile)

    # -r running file with others
    if args[1] == "-b" and args[4] == "-r" and args[5].endswith("xml"):
        problemfile = args[5]
        run(problemfile)
        dbterminate()
    elif args[3] == "-r" and args[4].endswith("xml"):
        problemfile = args[4]
        run(problemfile)
        dbterminate()

    if args[1] == "-r" and args[2].endswith("xml"):
        problemfile = args[2]
        run(problemfile)
        dbterminate()

if __name__ == "__main__":
    systemize()
