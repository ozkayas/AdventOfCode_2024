from collections import defaultdict, deque
from functools import cmp_to_key


def __main__():
    rules = readRules('05/rules.txt')
    # print(rules)
    jobs = readJobs('05/jobs.txt')
    # print(jobs)
    def comparator(num1: int, num2: int) -> int:
        # return -1, 1
        if num2 in rules[num1]:
            return -1
        else:
            return 1

    # PART 1 #
    total = 0
    fixedTotal = 0
    for job in jobs:
        # sort a copy of the job
        sorted_job = sorted(job, key=cmp_to_key(comparator))
        # check if sorted_job and job are the same
        if sorted_job == job:
            # Add middle item in the job to the total
            total += sorted_job[len(sorted_job) // 2]
        else:
            fixedTotal += sorted_job[len(sorted_job) // 2]
    print(f"Total: {total}")
    print(f"Fixed Total: {fixedTotal}")


def readRules(filename) -> dict[int, set[int]]:
    rules = defaultdict(set)
    with open(filename, 'r') as file:
        for line in file:
           u , v = (list(map(int, line.strip().split('|'))))
           rules[u].add(v)
    return rules

def readJobs(filename) -> list[list[int]]:
    orders = []
    with open(filename, 'r') as file:
        for line in file:
            orders.append(list(map(int, line.strip().split(','))))
    return orders

__main__()