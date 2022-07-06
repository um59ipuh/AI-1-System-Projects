import sys
from clues import *
from somehelp import *
import itertools
import copy

# Generate permutations for rows and cols
class PermutationGenerator:
    @staticmethod
    def set_init_pattern(clue_list, span):
        empty_line = [0] * span
        ptr = 0
        for i in range(len(clue_list)):
            clue = clue_list[i]
            cluenum = int(clue[0])
            if i != 0:
                prevclue = clue_list[i - 1]
                if clue[1] == prevclue[1]:
                    ptr += 1
            end = ptr + cluenum
            empty_line[ptr: end] = clue[1] * cluenum
            ptr = end

        return empty_line

    @staticmethod
    def only_clue_seq(clue_list, isline = False):
        if isline:
            res = ""
            for c in clue_list:
                if c != 0:
                    res += c
            return res
        else:
            return "".join([int(c[0])*c[1] for c in clue_list])

    @staticmethod
    def get_mapper(line):
        lst = [0]
        mem = line[0]
        for i in range(1, len(line)):
            if line[i] != 0 and line[i] != mem:
                lst.append(i)
                mem = line[i]
            elif line[i] != 0 and line[i-1] == 0 and line[i] == mem:
                lst.append(i)
                mem = line[i]
        return lst

    @staticmethod
    def is_valid(line, clue):
        cptr = 0
        lptr = 0
        while lptr < len(line) and cptr < len(clue):
            if line[lptr] == 0:
                lptr += 1
            else:  # contains clue
                if line[lptr] != clue[cptr][-1]:
                    return False
                else:  # match
                    if clue[cptr][:-1] == '1':  # for 1
                        tlptr = lptr + 1
                        tcptr = cptr + 1
                        if tcptr < len(clue) and clue[tcptr][-1] == clue[cptr][-1]:
                            if tlptr < len(line) and line[tlptr] != 0:  # not match with 0
                                return False
                            else:
                                cptr = tcptr
                                lptr = tlptr + 1
                        else:  # clue mismatch prev and next
                            cptr = tcptr
                            lptr = tlptr
                    else:  # with 2 or more, use while again
                        counter = lptr + int(clue[cptr][:-1])
                        if counter > len(line):
                            return False
                        while lptr < counter:
                            if line[lptr] != clue[cptr][-1]:
                                return False
                            else:
                                lptr += 1
                        cptr += 1

        return True

    @staticmethod
    def all_permutations(clue_list: [], span):
        #  if list of clues is empty then just simply return
        if len(clue_list) == 0:
            return [[0] * span]

        firstline = PermutationGenerator.set_init_pattern(clue_list, span)

        permutations = list(itertools.permutations(firstline))

        validator = set()
        result = []
        for vp in permutations:
            lstr = "".join([str(e) for e in vp])
            if PermutationGenerator.is_valid(vp, clue_list) and lstr not in validator:
                validator.add(lstr)
                result.append(list(vp))
        return result


def perm(clue, length):

    if len(clue) == 0:
        return [[0]*length]

    empt_arr = []

    for n in range(length):
        empt_arr.append(0)
    permutations = help_perm(clue, 0, 0, empt_arr)

    return permutations


def help_perm(clue, number, start, array):
    # extract length and color from current clue
    n, c = int(clue[number][:-1]), clue[number][-1]

    perms = []

    warray = array

    for l in range(len(array)):
        if l >= start:
            # set current position to color
            for s in range(start, len(array)):
                warray[s] = 0
            #warray = array
            warray[l] = c
            nstart = l+n
            for l2 in range(n):
                if l-l2-1 > 0 and l-l2-1 >= start:
                    #reset previous set values to 0
                    warray[l-l2-1] = 0
                if l+l2 < len(array):
                    warray[l+l2] = c
            if number+1 < len(clue):
                nnew, cnew = int(clue[number+1][:-1]), clue[number+1][-1]
                if cnew == c:
                    newperm = help_perm(clue, number+1, nstart+1, warray)
                else:
                    newperm = help_perm(clue, number+1, nstart, warray)
                for p in newperm:
                    if PermutationGenerator.is_valid(p, clue):
                        perms.append(p)
            else:
                if PermutationGenerator.is_valid(warray, clue):
                    perms.append(copy.deepcopy(warray))

    return perms


# create boolean expressions
def map_to_pl(clue, size):
    height, weight = size
    logicexprs = {}

    # map every cell with associated colors
    cell_to_color = {}

    # map to pl for rows
    rows = clue['rows']
    logicexprs['row'] = []
    for i in range(len(rows)):
        permutations = perm(rows[i], weight)

        list_exp = []
        for pattern in permutations:
            # convert it to logic
            expr = []
            for j in range(len(pattern)):
                p = pattern[j]

                if p == 0:
                    C = 'W'
                else: # if p != 0
                    C = p.upper()

                exp = f"X{i+1}Y{j+1}{C}"
                expr.append(exp)

                # add color to particular cell
                key = f"{i+1},{j+1}"
                if key in cell_to_color:
                    cell_to_color[key].add(C)
                else:
                    cell_to_color[key] = set()
                    cell_to_color[key].add(C)

            list_exp.append(expr)
        logicexprs['row'].append(list_exp)

    # map to pl for col
    cols = clue['cols']
    logicexprs['col'] = []
    for i in range(len(cols)):
        permutations = perm(cols[i], height)
        list_exp = []
        for pattern in permutations:
            # convert it to logic
            expr = []
            for j in range(len(pattern)):
                p = pattern[j]
                if p == 0:
                    C = 'W'
                else: #if p != 0
                    C = p.upper()
                exp = f"X{j + 1}Y{i + 1}{C}"
                expr.append(exp)

                # add color to particular cell
                key = f"{j + 1},{i + 1}"
                if key in cell_to_color:
                    cell_to_color[key].add(C)
                else:
                    cell_to_color[key] = set()
                    cell_to_color[key].add(C)

            list_exp.append(expr)
        logicexprs['col'].append(list_exp)

    # find the fix one
    fixed = []
    # row fixing
    for row in logicexprs['row']:
        if len(row) == 1:
            # add to fixed
            for el in row[0]:
                fixed.append(el)

    # fixing col value
    for row in logicexprs['col']:
        if len(row) == 1:
            # add to fixed
            for el in row[0]:
                fixed.append(el)

    # map to pl for all cell to color
    logicexprs['cell'] = []
    for r, rval in enumerate(clue['rows'], 1):
        for c, cval in enumerate(clue['cols'], 1):
            cellname = f"X{r}Y{c}"
            cell = f"{r},{c}"
            cellcolors = list(cell_to_color[cell])
            if len(cellcolors) == 2:
                logicexprs['cell'].append([f"-{cellname}{c}" for c in cellcolors])
            else:
                for i in range(len(cellcolors)):
                    for j in range(i+1, len(cellcolors)):
                        logicexprs['cell'].append([f"-{cellname}{cellcolors[i]}", f"-{cellname}{cellcolors[j]}"])

    return logicexprs


def map_to_pl_hex(clue, size):
    logicexprs = {}

    # map every cell with associated colors
    cell_to_color = {}

    # map to pl for rows
    rows = clue['side1']
    logicexprs['side1'] = []
    incmnt = 0
    startx = size - 1
    starty = -(size - 1)
    for i in range(len(rows)):
        permutations = perm(rows[i], size + incmnt)

        list_exp = []
        for pattern in permutations:
            # convert it to logic
            expr = []
            for j in range(len(pattern)):
                p = pattern[j]
                if p == 0:
                    C = 'W'
                else: # if p != 0
                    C = p.upper()
                exp = f"X{startx - i}Y{starty + j}{C}"
                expr.append(exp)

                # add color to particular cell
                key = f"{startx - i},{starty + j}"
                if key in cell_to_color:
                    cell_to_color[key].add(C)
                else:
                    cell_to_color[key] = set()
                    cell_to_color[key].add(C)

            list_exp.append(expr)

        if i >= size-1:
            incmnt -= 1
            starty += 1
        else:
            incmnt += 1

        logicexprs['side1'].append(list_exp)

    # map to pl for col
    cols = clue['side2']
    logicexprs['side2'] = []
    incmnt = 0
    startx = -(size-1)#size - 1
    starty = 0 #- (size - 1)
    for i in range(len(cols)):
        permutations = perm(cols[i], size + incmnt)
        # print(f"Col all : {permutations}")
        list_exp = []
        for pattern in permutations:
            # convert it to logic
            expr = []
            for j in range(len(pattern)):
                p = pattern[j]
                if p == 0:
                    C = 'W'
                else: #if p != 0
                    C = p.upper()
                exp = f"X{startx + j}Y{starty - j}{C}"
                expr.append(exp)

                # add color to particular cell
                key = f"{startx + j},{starty - j}"
                if key in cell_to_color:
                    cell_to_color[key].add(C)
                else:
                    cell_to_color[key] = set()
                    cell_to_color[key].add(C)

            list_exp.append(expr)

        if i >= (size - 1):
            incmnt -= 1
            #startx -= 1
            startx += 1
        else:
            incmnt += 1
            starty += 1

        logicexprs['side2'].append(list_exp)


    # map to pl for col
    cols2 = clue['side3']
    logicexprs['side3'] = []
    incmnt = 0
    startx = 0
    starty = size - 1
    for i in range(len(cols2)):
        permutations = perm(cols2[i], size + incmnt)

        # print(f"Col all : {permutations}")
        list_exp = []
        for pattern in permutations:
            # convert it to logic
            expr = []
            for j in range(len(pattern)):
                p = pattern[j]
                if p == 0:
                    C = 'W'
                else: #if p != 0
                    C = p.upper()
                exp = f"X{startx - j}Y{starty}{C}"
                expr.append(exp)

                # add color to particular cell
                key = f"{startx - j},{starty}"
                if key in cell_to_color:
                    cell_to_color[key].add(C)
                else:
                    cell_to_color[key] = set()
                    cell_to_color[key].add(C)

            list_exp.append(expr)

        if i >= size-1:
            incmnt -= 1
        else:
            incmnt += 1
            startx += 1
        starty -= 1

        logicexprs['side3'].append(list_exp)

    # find the fix one
    fixed = []
    # row fixing
    for row in logicexprs['side1']:
        if len(row) == 1:
            # add to fixed
            for el in row[0]:
                fixed.append(el)

    # fixing col value
    for row in logicexprs['side2']:
        if len(row) == 1:
            # add to fixed
            for el in row[0]:
                fixed.append(el)

    # side 3
    for row in logicexprs['side3']:
        if len(row) == 1:
            # add to fixed
            for el in row[0]:
                fixed.append(el)

    # map to pl for all cell to color
    logicexprs['cell'] = []
    incmnt = 0
    startx = size - 1
    starty = -(size - 1)
    for r in range(size*2-1):
        for c in range(size+incmnt):
            cellname = f"X{startx - r}Y{starty + c}"
            cell = f"{startx - r},{starty + c}"
            cellcolors = list(cell_to_color[cell])
            if len(cellcolors) == 2:
                logicexprs['cell'].append([f"-{cellname}{c}" for c in cellcolors])
            else:
                for i in range(len(cellcolors)):
                    for j in range(i+1, len(cellcolors)):
                        logicexprs['cell'].append([f"-{cellname}{cellcolors[i]}", f"-{cellname}{cellcolors[j]}"])
        if r >= size-1:
            incmnt -= 1
            starty += 1
        else:
            incmnt += 1

    return logicexprs


def all_last(list_logic: [str]) -> set:
    return set([S[-1] for S in list_logic])


"""
Convert DNF to CNF, using this conversion
https://en.wikipedia.org/wiki/Conjunctive_normal_form#Conversion_into_CNF
"""


itr = 1
def to_cnf_linear_way(pls: [[]]) -> [[]]:
    pl_mapper = {}
    cnf = []
    global itr

    auxcnf = []
    #itr = 1
    for pl in pls:
        aux = f"Z{itr}"
        pl_mapper[aux] = pl
        itr += 1
        auxcnf.append(aux)
    cnf.append(auxcnf)

    for key, val in pl_mapper.items():
        for v in val:
            cnf.append([f"-{key}", v])

    return cnf

def to_cnf_linear_way_hex(pls: [[]]):
    pl_mapper = {}
    cnf = []
    global itr

    auxcnf = []
    #itr = 1
    for pl in pls:
        aux = f"Z{itr}"
        pl_mapper[aux] = pl
        itr += 1
        auxcnf.append(aux)
    #cnf.append(auxcnf)

    for key, val in pl_mapper.items():
        for v in val:
            cnf.append([f"-{key}", v])

    return auxcnf, cnf


# convert boolean expression to CNF
def to_cnf(logicexprs):

    variables = set()
    clauses = []

    # convert all row logics to CNF
    rows = logicexprs['row']
    for patterns in rows:
        # if pattern is just single then check if it's possible to fix or not
        if len(patterns) == 1:
            # with no value
            if len(patterns[0]) == 0:
                continue
            # fix value
            # if len(all_last(patterns[0])) == 1:
            # add all value as a fix value
            for exp in patterns[0]:
                clauses.append([exp])
                variables.add(exp)
        else:
            # iterate all elements
            for clause in to_cnf_linear_way(patterns):
                clauses.append(clause)
                for e in clause:
                    variables.add(e if '-' not in e else e[1:])

    # convert all row logics to CNF
    cols = logicexprs['col']
    for patterns in cols:
        # if pattern is just single then fix the value
        if len(patterns) == 1:
            # with no value
            if len(patterns[0]) == 0:
                continue
            # fix value
            for exp in patterns[0]:
                clauses.append([exp])
                variables.add(exp)
        else:
            # iterate all elements
            for clause in to_cnf_linear_way(patterns):
                clauses.append(clause)
                for e in clause:
                    variables.add(e if '-' not in e else e[1:])

    # convert at most once to CNF
    for cell in logicexprs['cell']:
        clauses.append(cell)

    return variables, clauses


def to_cnf_hex(logicexprs):
    variables = set()
    clauses = []
    auxs = []
    # convert all row logics to CNF
    rows = logicexprs['side1']

    i = 0
    counter = 0
    for patterns in rows:
        # if pattern is just single then check if it's possible to fix or not
        if len(patterns) == 1:
            # with no value
            if len(patterns[0]) == 0:
                continue
            # fix value
            # if len(all_last(patterns[0])) == 1:
                # add all value as a fix value
            for exp in patterns[0]:
                clauses.append([exp])
                variables.add(exp)
        else:
            # iterate all elements
            #aux, cnfs = to_cnf_linear_way_hex(patterns)
            cnfs = to_cnf_linear_way(patterns)
            #auxs.extend(aux)
            for clause in cnfs:
                clauses.append(clause)
                for e in clause:
                    if e[0] == '-':
                        variables.add(e[1:])
                    else:
                        variables.add(e)
        i += 1

    # convert all row logics to CNF
    cols = logicexprs['side2']
    clauseside2 = []
    for patterns in cols:
        # if pattern is just single then fix the value
        if len(patterns) == 1:
            # with no value
            if len(patterns[0]) == 0:
                continue
            # fix value
            for exp in patterns[0]:
                clauses.append([exp])
                clauseside2.append([exp])
                variables.add(exp)
        else:
            # iterate all elements
            # aux, cnfs = to_cnf_linear_way_hex(patterns)
            cnfs = to_cnf_linear_way(patterns)
            #auxs.extend(aux)
            for clause in cnfs:
                clauses.append(clause)
                clauseside2.append(clause)
                for e in clause:
                    variables.add(e if '-' != e[0] else e[1:])

    # convert all row logics to CNF
    cols = logicexprs['side3']
    clside3 = []
    i = 0
    for patterns in cols:
        # if pattern is just single then fix the value
        if len(patterns) == 1:
            # with no value
            if len(patterns[0]) == 0:
                continue
            # fix value
            for exp in patterns[0]:
                clauses.append([exp])
                clside3.append([exp])
                variables.add(exp)
        else:
            # iterate all elements
            # aux, cnfs = to_cnf_linear_way_hex(patterns)
            cnfs = to_cnf_linear_way(patterns)
            #auxs.extend(aux)
            for clause in cnfs:
                clauses.append(clause)
                clside3.append(clause)
                for e in clause:
                    variables.add(e if '-' != e[0] else e[1:])
        i += 1

    # convert at most once to CNF
    for cell in logicexprs['cell']:
        clauses.append(cell)

    # clauses.append(auxs)
    return variables, clauses


def result_to_pl(result, mapper, size, type):
    if type == "rect":
        row, col = size
        pllist = [[0 for j in range(col)] for i in range(row)]

        for ele in result:
            if int(ele) > 0:
                cellval = mapper[int(ele)]
                x = y = ''
                for i, c in enumerate(cellval):
                    if c == 'Y':
                        x = int(cellval[1: i]) - 1
                        y = int(cellval[i+1: -1]) - 1
                        pllist[x][y] = cellval

        return pllist
    elif type == 'hex':
        rlist = []
        for ele in result:
            if int(ele) > 0:
                rlist.append(mapper[int(ele)])

        pllist = []
        incmt = 0
        startx = size - 1
        starty = -(size - 1)
        for r in range(2*size-1):
            collist = []
            for c in range(size + incmt):
                cell = f"X{startx - r}Y{starty + c}"
                for re in rlist:
                    if cell == re[:-1]:
                        collist.append(re)

            pllist.append(collist)

            if r >= size - 1:
                incmt -= 1
                starty += 1
            else:
                incmt += 1

        return pllist
    '''
    pllist.sort()

    # make row and column
    svgval = []
    itr = 0
    for i in range(row):
        cols = []
        for j in range(col):
            cols.append(pllist[itr])
            itr += 1
        svgval.append(cols)

    return svgval
    '''


def solve():
    # file name
    clue = sys.argv[1]
    name = clue.split('.')[0]
    puzzle = ClueReader.read_clue(clue)

    # now calculate for rectangle
    if puzzle['type'] == 'rect':
        logicexprs = map_to_pl(puzzle['clue'], puzzle['size'])
        print(logicexprs)
        vars, clauses = to_cnf(logicexprs)
        print(clauses)
        # write cnf to file and get mapped value
        mappingsol = wsat(name, (vars, clauses))

        # calculate sat and get solution line
        #sol = callsat(name)

        # result would be from 1 to before the last one
        #result = sol.split(' ')[1: -1]
        #pllist = result_to_pl(result, mapingsol, puzzle['size'])

        # draw svg
        #draw_rect_puzzle(puzzle['size'], pllist, puzzle['color'], name)

if __name__ == '__main__':
    solve()