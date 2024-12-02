from collections import Counter


def read_columns_from_file(filename):
    # Initialize empty lists for both columns
    report = []
    
    # Read the file and split into columns
    with open(filename, 'r') as file:
        for line in file:
            num = list(map(int, line.strip().split()))
            report.append(num)
    
    return report

# Read the file and get the columns
reports = read_columns_from_file('02/input.txt')

def safeIncreasing(report, tolerateOneLevel=False) -> bool:
    for i in range(1,len(report)):
        if report[i-1] < report[i] <= report[i-1] + 3:
            continue
        else:
            if tolerateOneLevel:
                prevPopped = report.copy()
                prevPopped.pop(i-1)
                currentPopped = report.copy()
                currentPopped.pop(i)
                if (safeIncreasing(prevPopped, tolerateOneLevel=False) or safeIncreasing(currentPopped, tolerateOneLevel=False)):
                    continue
            return False
    return True

def safeDecreasing(report, tolerateOneLevel=False) -> bool:
    for i in range(1,len(report)):
        if report[i-1] > report[i] >= report[i-1] - 3:
            continue
        else:
            if tolerateOneLevel:
                prevPopped = report.copy()
                prevPopped.pop(i-1)
                currentPopped = report.copy()
                currentPopped.pop(i)
                if (safeDecreasing(prevPopped, tolerateOneLevel=False) or safeDecreasing(currentPopped, tolerateOneLevel=False)):
                    continue
            return False
    return True

safeReports = 0
for report in reports:
    if safeIncreasing(report) or safeDecreasing(report):
        safeReports += 1

print(f"Safe reports: {safeReports}") ## // Result : 390

safeReportsWithOneLevel = 0
for report in reports:
    if safeIncreasing(report, True) or safeDecreasing(report, True):
        safeReportsWithOneLevel += 1

print(f"Safe reports with one level tolerance: {safeReportsWithOneLevel}")


print(safeIncreasing([1, 3, 2, 4, 5], True))