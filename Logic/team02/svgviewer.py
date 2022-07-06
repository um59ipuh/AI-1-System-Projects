import svgwrite


def draw_rect_puzzle(shape, puzzle, color_mapping, file):
    square = "50px"
    row, col = shape
    svg_document = svgwrite.Drawing(filename = f"./svgs/{file}.svg", size = (f"{5*col*50}px", f"{5*row*50}px"))

    start = (100, 100)
    for r in range(row):
        for c in range(col):
            cell = f"X{r+1}Y{c+1}"
            for p in puzzle[r]:
                if cell == p[:-1]:
                    cell = p
            # set the color
            ch = cell[-1]
            if ch == 'W':
                color = 'white'
                ch = ''
            else:
                color = color_mapping[ch.lower()]
            svg_document.add(svg_document.rect(insert = start,
                                       size = (square, square),
                                       stroke_width = "2.5",
                                       stroke = "black",
                                       fill = str(color)))
            center = (start[0]+20, start[1]+30)
            svg_document.add(svg_document.text(str(ch.lower()), insert=center, fill='white'))
            # set mouse pointer
            start = (start[0] + 50, start[1])
        start = (100, start[1] + 50)

    # print(svg_document.tostring())

    svg_document.save()
    print(f"{file}.svg drawing Complete! Located in svgs folder")


def drawPolygon(size, puzzle, color_mapping, file):
    svg_document = svgwrite.Drawing(filename=f"./svgs/{file}.svg",
                                    size=("1000px", "1000px"))

    width = 50
    height = 30
    padding = 100
    roof = height // 2
    initialX = padding + (size - 1) * roof
    initialY = 100

    startX = initialX
    startY = initialY

    prevlen = len(puzzle[0])
    for r in range(len(puzzle)):
        # change X and Y based on increase & decrese
        cols = len(puzzle[r])
        if r != 0 and prevlen < cols:
            # shift to left
            startX = initialX - (width // 2)
        elif r != 0 and prevlen > cols:
            startX = initialX + (width // 2)

        initialX = startX

        for c in range(cols):
            start1 = (startX, startY)
            start2 = (start1[0] + width // 2, start1[1] - roof)
            start3 = (start1[0] + width, start1[1])
            start4 = (start3[0], start3[1] + height)
            start5 = (start4[0] - width // 2, start4[1] + roof)
            start6 = (start1[0], start1[1] + height)

            # DRAWING
            cellc = puzzle[r][c][-1]
            if cellc == 'W':
                color = 'white'
                cellc = ''
            else:
                color = color_mapping[cellc.lower()]

            svg_document.add(svg_document.polygon(points=[start1, start2, start3, start4, start5, start6],
                                                  stroke_width='2',
                                                  stroke='black',
                                                  fill=f"{color}"))

            center = (startX + 20, startY + roof)
            svg_document.add(svg_document.text(f"{cellc.lower()}",
                                               insert=center,
                                               fill='white'))

            startX += width

        # start from begining of line
        prevlen = cols
        startY += (height + roof)

    # print(svg_document.tostring())

    svg_document.save()
    print(f"{file}.svg drawing Complete! Located in svgs folder")