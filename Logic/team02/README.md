# Assignment 4: Solve Picture Puzzles

## For running the code
### Prerequisites
> Use at least python version, python 3.7
 
Install svgwrite for drawing: `$ pip install svgwrite` 
### Steps
1. Open terminal under the root directory `team02` and execute the command with specified file like 
    `python clues.py {filename}` example depicts below
    > $ python clues.py ai.clues
2. Svg stored in svg file as filename.svg

### Constraints we consider
1. Take all valid permutations(relative position) for every clue line.
2. Consider as fixed value if line contains only one permutation
3. Take the constraints that one cell holds one color at a time.

### Unique Puzzles
1. All hex puzzles are unique.
2. For rectangles: Arrow, Assignment, ai, framed are all unique

### Way for determining uniqueness
We determine if there are isolated similar shapes in a general area, like the bushes in the forest puzzle on the lower right side.
If they exist the puzzle can be unique since those shapes can be swiched in some way.
All hex puzzles are unique cause every cell is fixed by three sided clues(triangulation)