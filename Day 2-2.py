inputFile = "Day 2 Input.txt"

input = []

with open(inputFile, 'r') as file:
    for line in file:
        report = list(map(int, line.split()))
        input.append(report)

maxChange = 3
minChange = 1

safeReports = 0

for report in input:
    for point in range(len(report) + 1):
        dummyReport = report.copy()
        
        if point < len(report):
            del dummyReport[point]

        safeReportFound = False

        goneUp = False
        goneDown = False

        isSafe = True

        for dummyPoint in range(1, len(dummyReport)):
            difference = dummyReport[dummyPoint - 1] - dummyReport[dummyPoint]

            if difference < 0:
                goneUp = True

            elif difference > 0:
                goneDown = True

            if (abs(difference) > maxChange) or (abs(difference) < minChange):
                isSafe = False
                print("unsafe" )

        if (goneUp != goneDown) and isSafe:
            safeReports += 1
            print(dummyReport)
            safeReportFound = True

            break
        
        if safeReportFound: break

print(safeReports)