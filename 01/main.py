from collections import Counter


def read_columns_from_file(filename):
    # Initialize empty lists for both columns
    column1 = []
    column2 = []
    
    # Read the file and split into columns
    with open(filename, 'r') as file:
        for line in file:
            # Split each line by whitespace and convert to integers
            num1, num2 = map(int, line.strip().split())
            column1.append(num1)
            column2.append(num2)
    
    return column1, column2

# Read the file and get the columns
col1, col2 = read_columns_from_file('01/input.txt')

col1.sort()
col2.sort()

diff = 0
for i in range(len(col1)):
    diff += abs(col2[i] - col1[i])

print(diff)

#Find similarity between two columns
similarity = 0
col2freq = Counter(col2)
for i in range(len(col2)):
    if col1[i] in col2freq:
        similarity += col1[i] * col2freq[col1[i]]

print(similarity)
