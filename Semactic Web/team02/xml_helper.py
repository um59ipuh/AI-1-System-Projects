import xml.etree.ElementTree as ET

class Coauth:
    def __init__(self, n):
        self.name = n
        self.next = None
        self.prev = None
        self.paper = ""


class Problem:
    def __init__(self, i, t, wq, qs, be = None, af = None, frm = None, to = None):
        '''id, type: string, withquery: boolean, queries: List of strings'''
        self.id = i
        self.type = t
        self.withquery = wq
        self.query = ""
        self.queries = qs
        self.solutions = []
        self.before = be
        self.after = af
        self.frm = frm
        self.to = to

    def __repr__(self):
        return f"Problem = id : {self.id}; type: {self.type}; queries: {self.queries}, " \
               f"| {self.before} | {self.after} | {self.frm}| {self.to}, sol = {self.solutions}"


def xml_read(name):
    f = ET.parse(name)
    p = f.findall("Problem")

    problems = []

    for pr in p:

        wq = False

        if pr.get("withquery") == "true":
            wq = True

        values = pr.findall("value")

        queries = []

        problem_type = pr.get("type")

        by = None
        ay = None
        frm = None
        to = None
        for v in values:
            vtype = v.get("type")
            if problem_type == "top-3-keywords":
                if vtype == "before":
                    by = v.text
                elif vtype == "after":
                    ay = v.text
                else:
                    queries.append(v.text)

            elif problem_type == "coauth-dist":
                if vtype == "from":
                    frm = v.text
                else:
                    to = v.text

            else:
                queries.append(v.text)

        problems.append(Problem(pr.get("id"), pr.get("type"), wq, queries, by, ay, frm, to))

    print(f"Read out {len(problems)} problems")

    return problems


def xml_write(problems):
    f = open("solutions.xml", "w")

    f.write("<Solutions>\n")

    for p in problems:
        f.write("\t<Solution id=\""+p.id+"\">\n")
        if p.type == 'coauthors':
            for s in p.solutions:
                f.write("\t\t<value type=\"coauthor\">"+s+"</value>\n")
        elif p.type == 'msc-intersection':
            for s in p.solutions:
                f.write("\t\t<value type=\"paper\">"+s+"</value>\n")
        elif p.type == 'top-3-keywords':
            for s in p.solutions:
                f.write("\t\t<value type=\"keyword\">"+s[0]+"</value>\n")
                f.write("\t\t<value type=\"count\">"+s[1]+"</value>\n")
        elif p.type == 'coauth-dist':
            for s in p.solutions:
                f.write("\t\t<value type=\"author\">"+s.name+"</value>\n")
                if s.paper != "":
                    f.write("\t\t<value type=\"paper\">"+s.paper+"</value>\n")

        if p.withquery:
            f.write("\t\t<query>"+ p.query +"</query>\n")
        f.write("\t</Solution>\n")
    f.write("</Solutions>")
    print("Solution.xml is created with all solutions.")
