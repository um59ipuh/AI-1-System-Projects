"Implement write method for file. So far pseudocode-ish"
import subprocess
import codecs

def wsat(name, cnf):
    variables, clauses = cnf

    expr_int = {}
    int_expr = {}
    for counter, var in enumerate(variables, 1):
        expr_int[var] = counter
        int_expr[counter] = var

    #print(f"exprint : {expr_int}")
    #print(f"Clause : {clauses}")
    #print(f"Variables: {variables}")

    f = open(name + ".sat", "w")
    'get the number of variables and clauses here'
    nc = len(clauses)
    nv = len(variables)
    #write
    f.write("p cnf " + str(nv) + " " + str(nc) + "\n")
    'write the clauses into the file'
    for c in clauses:
        for exp in c:
            if exp[0] == '-':
                f.write(f"-{str(expr_int[exp[1:]])}" + " ")
            else:
                f.write(str(expr_int[exp]) + " ")
        f.write("0\n")

    return int_expr


"Implement translation method XYC -> n"
def trans(cnf, colors: [str], height: int, weight: int):
    "Idea: Make dictonary for simple replacement of variables"
    'Get real numbers somehow'
    nc = colors #0 #number of colors. Better, use letters
    nx = weight #number of x
    ny = height #number of y

    work = cnf
    dic = {}
    i = 1
    for c in nc:
        for y in range(1, nx+1):
            for x in range(1, ny+1):
                dic["X"+str(x)+"Y"+str(y)+c] = str(i)
                i += 1


    # print(f"CNF: {cnf}")
    # print(f"DIC: {dic}")
    'translation of the cnf array'
    for clause in range(len(cnf)):
        for variable in range(len(cnf[clause])):
            empty = ""
            if '-' in cnf[clause][variable]:
                exp = cnf[clause][variable][1:]
                empty = '-'
            else:
                exp = cnf[clause][variable]
            work[clause][variable] = empty + dic[exp]


    print(f"Work : {work}")
    return work

    "now we have a dictionary for the translation and can replace X0Y0A with 1, for example"
    "iterate through problem and replace entries or somth. Depends on how problem is given"
    "be careful about negations i think"
    "[[X1Y1A,X2Y0B],[],[]]"

def callsat(name):

    process = subprocess.run(['../kissat/build/kissat', f"{name}.sat", '--relaxed'], stdout=subprocess.PIPE)
    pr = False
    solution = ''
    for line in process.stdout.splitlines():
        # print(f"Solution Line: {codecs.decode(line, 'UTF-8')}")
        strline = codecs.decode(line, 'UTF-8')
        if pr == True:
            if strline[0] == 'c':
                break
            else:
                solution += strline[1:]
        if 'SATISFIABLE' in strline:
            pr = True

    return solution


def wsol(name, solution):

    f = open(name + ".sol", "w")
    f.write(solution + "\n")


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


if __name__ == '__main__':
    a = perm(['2b', '1b', '1b', '1a', '1a'], 12)
    print(a)
