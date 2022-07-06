def convert_sol_format(plan: str, x: int):
    # convert all planning to shoot walk and direction
    actions = ['move', 'shoot-arrow']

    words = plan.strip().strip('()').split(' ')

    action = words[0]

    if 'move' in action:

        from_ = words[2].split('_')
        to = words[3].split('_')

        if 'out' in to:
            if int(from_[1]) == 0:
                return f"walk up\n"
            elif int(from_[2]) == 0:
                return f"walk left\n"
            elif int(from_[2]) == x:
                return f"walk right\n"
            else:
                return f"walk down\n"
        else:
            if int(to[1]) - int(from_[1]) > 0:
                return f"walk down\n"
            elif int(to[2]) - int(from_[2]) > 0:
                return f"walk right\n"
            elif int(to[1]) - int(from_[1]) < 0:
                return "walk up\n"
            elif int(to[2]) - int(from_[2]) < 0:
                return f"walk left\n"

    elif 'shoot-arrow' in action:

        from_ = words[3].split('_')
        to = words[4].split('_')

        if int(to[1]) - int(from_[1]) > 0:
            return f"shoot down\n"
        elif int(to[2]) - int(from_[2]) > 0:
            return f"shoot right\n"
        elif int(to[1]) - int(from_[1]) < 0:
            return "shoot up\n"
        elif int(to[2]) - int(from_[2]) < 0:
            return f"shoot left\n"


def overwrite(file, x):
    with open(file, 'r+') as f:
        lines = f.readlines()
        formattedlines = []
        for line in lines:
            formattedlines.append(convert_sol_format(line, x))

        f.seek(0)

        for line in formattedlines:
            if line is not None:
                f.write(line)

        f.truncate()


if __name__ == "__main__":
    overwrite("map00test.pddl.soln", 7)
