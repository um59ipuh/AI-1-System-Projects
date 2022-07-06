def map_to_pl_hex(clue, size):
    '''TODO: Implement coordinates correctly'''
    index_based = 1
    height, weight = size
    logicexprs = {}

    # map every cell with associated colors
    cell_to_color = {}

    # map to pl for rows
    rows = clue['side1']
    logicexprs['side1'] = []
    for i in range(len(rows)):
        permutations = perm(rows[i], weight)

        # print(f"Row all : {permutations}")
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
        logicexprs['side1'].append(list_exp)

    # map to pl for col
    cols = clue['side2']
    logicexprs['side2'] = []
    for i in range(len(cols)):
        permutations = perm(cols[i], height)
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
        logicexprs['side2'].append(list_exp)

    # map to pl for col
    cols2 = clue['side3']
    logicexprs['side3'] = []
    for i in range(len(cols2), 0, -1):
        permutations = perm(cols2[i], height)
        # print(f"Col all : {permutations}")
        list_exp = []
        for pattern in permutations:
            # convert it to logic
            expr = []
            for j in range(len(pattern), 0, -1):
                p = pattern[j]
                if p == 0:
                    C = 'W'
                else: #if p != 0
                    C = p.upper()
                exp = f"X{j}Y{i}{C}"
                expr.append(exp)

                # add color to particular cell
                key = f"{j},{i}"
                if key in cell_to_color:
                    cell_to_color[key].add(C)
                else:
                    cell_to_color[key] = set()
                    cell_to_color[key].add(C)

            list_exp.append(expr)
        logicexprs['side3'].append(list_exp)

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

    print(f"Fixed : {fixed}")
    # eliminate if cell does contain fixed value but pattern doesn't

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
