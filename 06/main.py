def readLineAsList(filename):
    items_list = []
    with open(filename, 'r') as file:
        for line in file:
           items = list(line.strip())
           items_list.append(items)
    return items_list

def readTextFile(filename) -> str:
    with open(filename, 'r') as file:
        return file.read()

def findStartPoint(grid) -> tuple[str, int, int]:
    for i, row in enumerate(grid):
        for j, item in enumerate(row):
            if item not in '.#':
                return (item, i, j)
            
def nextPoint(char, r, c) -> tuple[int, int]:
    if char == '^':
        return (r - 1, c)
    elif char == 'v':
        return (r + 1, c)
    elif char == '<':
        return (r, c - 1)
    elif char == '>':
        return (r, c + 1)
    
def turnRight(char) -> str:
    if char == '^':
        return '>'
    elif char == 'v':
        return '<'
    elif char == '<':
        return '^'
    elif char == '>':
        return 'v'

def isInBounds(r, c, grid) -> bool:
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def hasCycle(dir, r, c, grid) -> bool:
    seen = dict()  # (r, c) -> direction
    steps = 0
    MAX_STEPS = 1000  # Safety limit to prevent infinite loops
    
    while steps < MAX_STEPS:
        # If we've seen this position with this direction before, it's a cycle
        if (r, c) in seen and seen[(r, c)] == dir:
            return True
            
        seen[(r, c)] = dir
        nr, nc = nextPoint(dir, r, c)
        
        if not isInBounds(nr, nc, grid):
            return False
            
        if grid[nr][nc] == '#':
            dir = turnRight(dir)
            continue
            
        r, c = nr, nc
        steps += 1
        
    return False  # If we exceed MAX_STEPS, assume no cycle

def printGrid(grid):
    for row in grid:
        print(''.join(row))
    print()

def __main__():
    grid = readLineAsList('06/input_test.txt')
    # grid = readLineAsList('06/input.txt')
    
    # PART 1 #
    dir, r, c = findStartPoint(grid)
    initial_dir = dir
    initial_r, initial_c = r, c
    
    # Get the first position after start - this is where we'll begin cycle checks from
    start_r, start_c = nextPoint(initial_dir, initial_r, initial_c)
    
    # First collect the original path
    visited = dict()  # (r, c) -> direction
    curr_r, curr_c = start_r, start_c
    curr_dir = initial_dir
    
    while True:
        visited[(curr_r, curr_c)] = curr_dir
        nr, nc = nextPoint(curr_dir, curr_r, curr_c)
        if not isInBounds(nr, nc, grid):
            break
        if grid[nr][nc] == '#':
            curr_dir = turnRight(curr_dir)
            continue
        curr_r, curr_c = nr, nc
    
    print(f"Part 1: Visited {len(visited)} positions")

    # PART 2 #
    obstacleCount = 0
    tested = set()  # Keep track of tested positions
    
    # Only test positions that are empty in the original grid
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            # Skip if:
            # 1. Not an empty space
            # 2. Is the start position
            # 3. Is the first position after start
            if (grid[r][c] != '.' or 
                (r == initial_r and c == initial_c) or 
                (r == start_r and c == start_c)):
                continue
                
            # Try placing obstacle
            grid[r][c] = '#'
            if hasCycle(initial_dir, start_r, start_c, grid):
                obstacleCount += 1
                print(f"Found valid cycle with obstacle at ({r}, {c})")
            grid[r][c] = '.'

    print(f"Final Obstacle Count: {obstacleCount}")

if __name__ == "__main__":
    __main__()