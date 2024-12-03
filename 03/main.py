def readTextFile(filename) -> str:
    with open(filename, 'r') as file:
        return file.read()

txt = readTextFile('03/input.txt')
mulIndex = []

enabled = True

for i in range(len(txt)):
    if txt[i] == "d":
        if i+7 < len(txt) and txt[i:i+7] == "don't()":
            enabled = False
        elif i+4 < len(txt) and txt[i:i+4] == "do()":
            enabled = True
    if txt[i] == "m":
        if enabled:
            if (i+3 <= len(txt)) and txt[i:i+3] == "mul":
                mulIndex.append(i)

result = 0
for index, i in enumerate(mulIndex):
    # print(txt[i:i+3])
    # Pass if the next character is not a "("
    if i+3 >= len(txt) or txt[i+3] != "(":
        # print("Error at index: ", i)
        continue

    startIndex = i+3
    # Find the closing parenthesis
    closeIndex = txt.find(")", i)
    # Check if there's no closing parenthesis
    if closeIndex == -1:
        # print("Error: No closing parenthesis found at index:", i)
        continue
        
    # Check if the closing parenthesis is after the next mul
    if index + 1 < len(mulIndex) and closeIndex > mulIndex[index + 1]:
        # print("Error: Closing parenthesis found after next mul at index:", i)
        continue

    # Get the numbers between the parentheses
    numbers = txt[startIndex+1:closeIndex].split(",")
    if len(numbers) != 2:
        # print("Error: Invalid number of arguments at index:", i)
        continue

    if numbers[0].isdigit() and numbers[1].isdigit():
        result += int(numbers[0]) * int(numbers[1])
    else:
        # print("Error: Invalid numbers at index:", i)
        continue

print(f"Result: {result}")