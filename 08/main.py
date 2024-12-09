from collections import defaultdict
from itertools import combinations


def readLineAsList(filename):
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            # Convert each line into a list of individual characters
            items = list(line.strip())
            grid.append(items)
    return grid

def findAntiNodes(pos1, pos2, grid) -> list[tuple[int, int]]:
    nodes = []
    x1, y1 = pos1
    x2, y2 = pos2
    diffX = x2 - x1
    diffY = y2 - y1
    node1x, node1y = x2 + diffX, y2 + diffY
    node2x, node2y = x1 - diffX, y1 - diffY
    if 0 <= node1x < len(grid) and 0 <= node1y < len(grid[0]):
        nodes.append((node1x, node1y))
    if 0 <= node2x < len(grid) and 0 <= node2y < len(grid[0]):
        nodes.append((node2x, node2y))
    return nodes

def findAntiNodes2(pos1, pos2, grid) -> list[tuple[int, int]]:
    nodes = []
    x1, y1 = pos1
    x2, y2 = pos2
    diffX = x2 - x1
    diffY = y2 - y1
    # go in pos2 direction, while staying in grid, including pos2
    while 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]):
        nodes.append((x2, y2))
        x2 += diffX
        y2 += diffY
    # go in pos1 direction, while staying in grid, including pos1
    while 0 <= x1 < len(grid) and 0 <= y1 < len(grid[0]):
        nodes.append((x1, y1))
        x1 -= diffX
        y1 -= diffY
    return nodes

def __main__():

    ###### PART 1 ######
    # grid = readLineAsList("08/input_test.txt")
    grid = readLineAsList("08/input.txt")
    antennas = defaultdict(list) # to hold positions of antennas a:[(0,0), (0,1), (0,2)]
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] != ".":
                antennas[grid[r][c]].append((r, c))
    # print(antennas)

    nodesSet = set()
    ## get combinations of positions for each antenna
    for antenna in antennas:
        for pos1, pos2 in combinations(antennas[antenna], 2):
            # print(antenna, pos1, pos2)
            antiNodes = findAntiNodes(pos1, pos2, grid)
            # print(antiNodes)
            nodesSet.update(antiNodes)
    print(f"Part 1: {len(nodesSet)}")


    ###### PART 2 ######
    nodesSet = set()
    for antenna in antennas:
        for pos1, pos2 in combinations(antennas[antenna], 2):
            antiNodes = findAntiNodes2(pos1, pos2, grid)
            nodesSet.update(antiNodes)
    print(f"Part 2: {len(nodesSet)}")



__main__()