import sys
from solver import *
from somehelp import *
from svgviewer import *


class Clue:
    def __init__(self, name: str, type: str, size: tuple, cols: [str], values: {}):
        self.name = name
        self.type = type
        self.size = size
        self.cols = cols
        self.values = values


class ClueReader:

    @staticmethod
    def read_clue(clue: str) -> {}:
        path = f"./puzzles/{clue}"

        # data structure for storing all info for a particular puzzle
        puzzle = {}

        with open(path, 'r') as f:
            lines = f.readlines()
            firstline = lines[0].split(' ')
            type = firstline[0]
            if type == 'rect':
                sizer, sizec = firstline[1:3]
                puzzle['size'] = (int(sizer), int(sizec))
            elif type == 'hex':
                sizeh = int(firstline[1])
                puzzle['size'] = sizeh

            puzzle['type'] = type

            colors = {}
            colval = "abcdefghijklmnopqrstuvwxyz"
            itr = 0
            for color in lines[1].strip().split(' '):
                # ignore color:: `white`
                if color == '#ffffff':
                    colors["W"] = color
                else:
                    colors[colval[itr]] = color
                    itr += 1

            puzzle['color'] = colors

            clues = {}
            if type == 'rect':
                # select as row and col
                # do the parsing for rectangular model
                # do the parsing and return like a dict {cols: rows:}
                # parse row values
                row_start_index = 2

                clues['rows'] = []
                for i in range(row_start_index, row_start_index + int(sizer)):
                    values = lines[i].strip().split(' ')
                    if len(values) == 1 and values[0] == '':
                        clues['rows'].append([])
                    else:
                        clues['rows'].append(values)

                # parse column values
                col_start_index = row_start_index + int(sizer)
                clues['cols'] = []
                for i in range(col_start_index, col_start_index + int(sizec)):
                    values = lines[i].strip().split(' ')
                    if len(values) == 1 and values[0] == '':
                        clues['cols'].append([])
                    else:
                        clues['cols'].append(values)

                puzzle['clue'] = clues

            elif type == 'hex':

                sizeh = sizeh * 2 - 1

                #size*2-1
                clues['side1'] = []
                side_1_index = 2
                clues['side2'] = []
                side_2_index = side_1_index + sizeh
                clues['side3'] = []
                side_3_index = side_2_index + sizeh

                for i in range(side_1_index, side_1_index + sizeh):
                    values = lines[i].strip().split(' ')
                    if len(values) == 1 and values[0] == '':
                        clues['side1'].append([])
                    else:
                        clues['side1'].append(values)
                # print(f"Puzzle : {puzzle}")

                for i in range(side_2_index, side_2_index + sizeh):
                    values = lines[i].strip().split(' ')
                    if len(values) == 1 and values[0] == '':
                        clues['side2'].append([])
                    else:
                        clues['side2'].append(values)

                for i in range(side_3_index, side_3_index + sizeh):
                    values = lines[i].strip().split(' ')
                    if len(values) == 1 and values[0] == '':
                        clues['side3'].append([])
                    else:
                        clues['side3'].append(values)

                puzzle['clue'] = clues

            # print(f"Puzzles: {puzzle}")
            return puzzle


if __name__ == '__main__':
    clue = sys.argv[1]
    name = clue.split('.')[0]
    puzzle = ClueReader.read_clue(clue)
    print(f"Read from clues complete for file : {name}")

    if puzzle['type'] == 'rect':
        logicexprs = map_to_pl(puzzle['clue'], puzzle['size'])
        vars, clauses = to_cnf(logicexprs)
        colors = [c.upper() for c in list(puzzle['color'].keys())]
        # value = trans(clauses, colors, height=puzzle['size'][0], weight=puzzle['size'][1])
        mapingsol = wsat(name, (vars, clauses))

        sol = callsat(name)

        # result would be from 1 to before the last one
        result = sol.strip().split(' ')[: -1]
        pllist = result_to_pl(result, mapingsol, puzzle['size'], "rect")
        # draw svg
        draw_rect_puzzle(puzzle['size'], pllist, puzzle['color'], name)

    if puzzle['type'] == 'hex':
        logicexprs = map_to_pl_hex(puzzle['clue'], puzzle['size'])
        vars, clauses = to_cnf_hex(logicexprs)
        colors = [c.upper() for c in list(puzzle['color'].keys())]

        mapingsol = wsat(name, (vars, clauses))

        sol = callsat(name)

        # result would be from 1 to before the last one
        result = sol.strip().split(' ')[: -1]
        pllist = result_to_pl(result, mapingsol, puzzle['size'], "hex")

        # draw svg
        drawPolygon(puzzle['size'], pllist, puzzle['color'], name)
