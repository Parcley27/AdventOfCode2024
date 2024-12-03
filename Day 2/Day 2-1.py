import os

inputFile = "Day 2 Input.txt"

script_dir = os.path.dirname(__file__)
inputFile = os.path.join(script_dir, inputFile)

input = []

with open(inputFile, 'r') as file:
    for line in file:
        report = list(map(int, line.split()))
        input.append(report)

maxChange = 3
minChange = 1

safeReports = 0

for report in input:
    goneUp = False
    goneDown = False

    isSafe = True

    for point in range(1, len(report)):
        difference = report[point - 1] - report[point]

        if difference < 0:
            goneUp = True

        elif difference > 0:
            goneDown = True

        if abs(difference) > maxChange or abs(difference) < minChange:
            isSafe = False

    if (goneUp != goneDown) and isSafe:
        safeReports += 1

print(safeReports)