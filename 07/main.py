def read_input_file(file_path):
    result_dict = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Boş satırları atla
                # Her satırı ":" karakterinden böl
                key, values = line.strip().split(':')
                # Key'i integer'a çevir
                key = int(key)
                # Values kısmını boşluklardan böl ve integer listesine çevir
                values = [int(x) for x in values.strip().split()]
                # Listeyi deque'ye çevir
                result_dict[key] = values
    
    return result_dict

def recPart1(value, remaining) -> bool:
    if len(remaining) == 2:
        return value == remaining[0]*remaining[1] or value == sum(remaining)
    
    last= remaining.pop()

    if value % last != 0:
        return recPart1(value - last, remaining[:])
    else:
        return recPart1(value // last, remaining[:]) or recPart1(value - last, remaining[:])

def recPart2(value, remaining) -> bool:
    # print(f"value: {value}, remaining: {remaining}")
    if len(remaining) == 2:
        return value == remaining[0]*remaining[1] or value == sum(remaining) or "".join(map(str,remaining)) == str(value)
    
    last = remaining.pop()
    
    if value % last != 0:
        # If the number ends with the last digit, try both subtraction and concatenation removal
        if str(value).endswith(str(last)):
            return recPart2(value - last, remaining[:]) or recPart2(value//(10**len(str(last))), remaining[:])
        # Otherwise just try subtraction
        else:
           return recPart2(value - last, remaining[:])
    
    # If number doesn't end with last digit, try subtraction and division
    elif not str(value).endswith(str(last)):
        return recPart2(value - last, remaining[:]) or recPart2(value//last, remaining[:])
    
    # If we get here, number is divisible by last AND ends with last
    else:
        return recPart2(value - last, remaining[:]) or recPart2(value//last, remaining[:]) or recPart2(value//(10**len(str(last))), remaining[:])
    

def __main__():
    # table = read_input_file('07/input_test.txt')
    table = read_input_file('07/input.txt')

    #PART 1 #
    # keys = []
    # for key, value in table.items():
    #     if recPart1(key, value):
    #         keys.append(key)
    # print(f"PART 1: {sum(keys)}")

    # PART 2 #
    keys = []
    for key, value in table.items():
        if recPart2(key, value):
            keys.append(key)
    print(f"PART 2: {sum(keys)}")
    
__main__()


equations = []

with open("07/input.txt", "r") as f:
  for line in f.readlines():
    line = line.strip()
    l, r = tuple(line.split(": "))
    equations.append((int(l), [*map(int, r.split(" "))]))

def evaluate(a, b, op):
  # left to right

  if op == '+':
    a += b
  elif op == '*':
    a *= b
  elif op == '||':
    a = int(str(a) + str(b))

  return a

possible_ops = ['+', '*']

def is_eqt_true(numbers, wanted=0, carry=0):
  if carry > wanted:
    return False
  if len(numbers) == 0:
    return carry == wanted

  number = numbers[0]

  b = False

  for o in possible_ops:
    nb = evaluate(carry, number, o)
    b = b or is_eqt_true(numbers[1:], wanted=wanted, carry=nb)

  return b

def get_sum():
  true_eqts_sum = 0

  for eqt in equations:
    if is_eqt_true(eqt[1], eqt[0]):
      true_eqts_sum += eqt[0]
  return true_eqts_sum

print('Part 1', get_sum())

possible_ops = ['||', '+', '*']

print('Part 2', get_sum())


def part2(puzzle_input):
    def is_valid(target, nums):
        n = len(nums)
        queue = [(1, nums[0])]
        while queue:
            i, val = queue.pop()
            if i == n:
                if val == target:
                    return True
                continue
            
            possibilities = [
                val + nums[i],
                val * nums[i],
                int(f'{val}{nums[i]}'),
            ]
            for p in possibilities:
                if p <= target:
                    queue.append((i+1, p))

        return False

    total = 0
    with open(puzzle_input, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                left, right = line.strip().split(': ')
                target = int(left)
                nums = [int(num) for num in right.split()]
                if is_valid(target, nums):
                    total += target

    return total

print(part2('07/input.txt'))  # Added print to see result