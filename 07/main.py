def readLineAsList(filename):
    items_list = []
    with open(filename, 'r') as file:
        for line in file:
           items = (list(map(int, line.strip().split())))
           items_list.append(items)
    return items_list

def readTextFile(filename) -> str:
    with open(filename, 'r') as file:
        return file.read()

def __main__():
    pass
    # PART 1 #




__main__()