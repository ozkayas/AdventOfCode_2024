def readTextFile(filename) -> list[list[str]]:
    table = []
    with open(filename, 'r') as file:
        for line in file:
            table.append(list(line.strip()))
    return table

table = readTextFile('04/input.txt')
#### PART 1 ####
target = "XMAS"

def exploreNorth(r, c):
    if r - 3 < 0:
        return False
    if table[r-1][c] == target[1] and table[r-2][c] == target[2] and table[r-3][c] == target[3]:
        return True
    return False

def exploreSouth(r, c):
    if r + 3 >= len(table):
        return False
    if table[r+1][c] == target[1] and table[r+2][c] == target[2] and table[r+3][c] == target[3]:
        return True
    return False

def exploreEast(r, c):
    if c + 3 >= len(table[r]):
        return False
    if table[r][c+1] == target[1] and table[r][c+2] == target[2] and table[r][c+3] == target[3]:
        return True
    return False

def exploreWest(r, c):
    if c - 3 < 0:
        return False
    if table[r][c-1] == target[1] and table[r][c-2] == target[2] and table[r][c-3] == target[3]:
        return True
    return False

def exploreNorthEast(r, c):
    if r - 3 < 0 or c + 3 >= len(table[r]):
        return False
    if table[r-1][c+1] == target[1] and table[r-2][c+2] == target[2] and table[r-3][c+3] == target[3]:
        return True
    return False

def exploreNorthWest(r, c):
    if r - 3 < 0 or c - 3 < 0:
        return False
    if table[r-1][c-1] == target[1] and table[r-2][c-2] == target[2] and table[r-3][c-3] == target[3]:
        return True
    return False

def exploreSouthEast(r, c):
    if r + 3 >= len(table) or c + 3 >= len(table[r]):
        return False
    if table[r+1][c+1] == target[1] and table[r+2][c+2] == target[2] and table[r+3][c+3] == target[3]:
        return True
    return False    

def exploreSouthWest(r, c):
    if r + 3 >= len(table) or c - 3 < 0:
        return False
    if table[r+1][c-1] == target[1] and table[r+2][c-2] == target[2] and table[r+3][c-3] == target[3]:
        return True
    return False

def explore(r, c) -> int:
    found = 0
    if exploreNorth(r, c):
        found += 1
    if exploreSouth(r, c):
        found += 1
    if exploreEast(r, c):
        found += 1
    if exploreWest(r, c):
        found += 1
    if exploreNorthEast(r, c):
        found += 1
    if exploreNorthWest(r, c):
        found += 1
    if exploreSouthEast(r, c):
        found += 1
    if exploreSouthWest(r, c):
        found += 1
    return found

counter = 0

for r in range(len(table)):
    for c in range(len(table[r])):
        if table[r][c] == target[0]:
            counter += explore(r, c)

print(f"counter: {counter}")

#### PART 2 ####
def xmasFinder(r,c) -> int:
    if r == 0 or c == 0 or r == len(table) - 1 or c == len(table[r]) - 1:
        return 0
    if {table[r-1][c-1],table[r+1][c+1]} == {"M","S"} and {table[r-1][c+1],table[r+1][c-1]} == {"M","S"}:
        return 1
    return 0

counter = 0
for r in range(len(table)):
    for c in range(len(table[r])):
        if table[r][c] == "A":
            counter += xmasFinder(r, c)

print(f"counter: {counter}")