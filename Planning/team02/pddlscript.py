from solutionscript import *
import sys
import subprocess

# for map 00
# todo: have to change for all maps


def all_connection(file, grid):
    row = len(grid)
    col = len(grid[0])
    for r in range(row):
        for c in range(col):
            # normal connection
            up = r - 1, c
            left = r, c - 1
            right = r, c + 1
            down = r + 1, c

            pos = [up, right, down, left]

            for p in pos:
                if 0 <= p[0] < row and 0 <= p[1] < col:
                    if grid[r][c] != 'X' and grid[p[0]][p[1]] != 'X':
                        file.write(
                            f"\t\t(conn grid_{r+1}_{c+1} grid_{p[0]+1}_{p[1]+1})\n")
                        #file.write(f"\t\t(conn grid_{p[0]+1}_{p[1]+1} grid_{r+1}_{c+1})\n")

            # push connection
            up = r - 2, c
            left = r, c - 2
            right = r, c + 2
            down = r + 2, c

            pos = [up, right, down, left]

            for p in pos:
                if 0 <= p[0] < row and 0 <= p[1] < col:
                    if grid[r][c] != 'X' and grid[p[0]][p[1]] != 'X':
                        file.write(
                            f"\t\t(push_conn grid_{r+1}_{c+1} grid_{p[0]+1}_{p[1]+1})\n")


def read_map(mapfile):
    fullpath = f"./assignment/{mapfile}.txt"
    grid = []
    with open(fullpath) as file:
        for line in file.readlines():
            grid.append([ch for ch in line if ch != '\n'])
    return grid


def pddl_write(mapname):

    grid = read_map(mapname)

    f = open(mapname + ".pddl", "w")

    wumpus = []
    crate = []
    pit = []
    wall = []
    arrow = []
    free = []
    door1 = []
    door2 = []
    goal = []
    sp = ""

    'init of the player and coordinate objects'
    f.write("(define (problem grid)\n")
    f.write("\t(:domain World)\n")
    f.write("\t(:objects\n")
    f.write("\t; all grid positions are coordinates\n")

    for y in range(len(grid)):
        f.write("\t\t")
        for x in range(len(grid[y])):
            f.write("grid_"+str(y+1)+"_"+str(x+1)+" ")
            if grid[y][x] == 'X':
                wall.append("grid_"+str(y+1)+"_"+str(x+1))
            elif grid[y][x] == 'W':
                wumpus.append("grid_" + str(y+1) + "_" + str(x+1))
            elif grid[y][x] == 'C':
                crate.append("grid_" + str(y+1) + "_" + str(x+1))
            elif grid[y][x] == 'P':
                pit.append("grid_" + str(y+1) + "_" + str(x+1))
            elif grid[y][x] == 'A':
                arrow.append("grid_" + str(y+1) + "_" + str(x+1))
            elif grid[y][x] == 'S':
                sp = "grid_" + str(y+1) + "_" + str(x+1)
                free.append(sp)
            elif grid[y][x] == ' ':
                free.append("grid_" + str(y+1) + "_" + str(x+1))
            elif grid[y][x] == '1':
                door1.append("grid_" + str(y + 1) + "_" + str(x + 1))
            elif grid[y][x] == '2':
                door2.append("grid_" + str(y+1) + "_" + str(x+1))
            if (y == 0 or x == 0 or y == len(grid)-1 or x == len(grid[y])-1) and grid[y][x] != 'X':
                goal.append("grid_" + str(y+1) + "_" + str(x+1))

        f.write("- coordinate\n")
    f.write("\t\tout - coordinate\n")

    f.write("\n\t\tS - bot\n")
    ac = 0
    for a in arrow:
        f.write("\t\tA"+str(ac)+" - arrow\n")
        ac += 1
    f.write(")\n")

    'init of the map predicates'
    f.write("\n\t(:init\n")
    f.write("\t\t; start position for player\n")
    f.write("\t\t(at S "+sp+")\n")
    f.write("\t\t(m1 S)\n")
    ac = 0
    for a in arrow:
        f.write("\t\t(at A"+str(ac)+" "+a+")\n")
        ac += 1
    f.write("\t\t; init grid connections\n")
    all_connection(f, grid)

    f.write("\t\t; add wumpus onto map\n")
    for w in wumpus:
        f.write("\t\t(wumpus "+w+")\n")
        # f.write("\t\t(blocked "+w+")\n")

    f.write("\t\t; add walls onto map\n")
    for w in wall:
        # f.write("\t\t(blocked " + w + ")\n")
        pass

    f.write("\t\t; add pits onto map\n")
    for p in pit:
        f.write("\t\t(pit "+p+")\n")
        # f.write("\t\t(blocked "+p+")\n")

    f.write("\t\t; add crates onto map\n")
    for c in crate:
        f.write("\t\t(crate "+c+")\n")
        # f.write("\t\t(blocked "+c+")\n")

    f.write("\t\t; add unblocked spaces onto map\n")
    for fs in free:
        f.write("\t\t(nblocked "+fs+")\n")
    for a in arrow:
        f.write("\t\t(nblocked "+a+")\n")

    f.write("\t\t(nblocked out)\n")

    f.write("\t\t; add doors\n")
    for d in door1:
        f.write("\t\t(d1 "+d+")\n")
    for d in door2:
        f.write("\t\t(d2 "+d+")\n")

    f.write("\t\t; add connections to goal state\n")
    for g in goal:
        f.write("\t\t(conn "+g+" out)\n")
        f.write("\t\t(conn out "+g+")\n")

    f.write("\t)\n")

    f.write("\t(:goal\n")
    f.write("\t(at S out)\n")

    f.write("\t)")
    f.write(")")

    f.close()

    return len(grid[y])


if __name__ == "__main__":
    #grid = read_map("map00")

    map_ = sys.argv[1]
    x = pddl_write(f"{map_}")
    process = subprocess.run(
        ['pyperplan', f"domain.pddl", f'{map_}.pddl'], stdout=subprocess.PIPE)
    overwrite(f"{map_}.pddl.soln", x)
