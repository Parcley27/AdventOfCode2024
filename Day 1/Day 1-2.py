import os

inputFile = "Day 1 Input.txt"

script_dir = os.path.dirname(__file__)
inputFile = os.path.join(script_dir, inputFile)

input = []

with open(inputFile, 'r') as file:
    for line in file:
        input.extend(map(int, line.split()))

print(input)

locationsA = []
locationsB = []

for number in range(len(input)):
    if number % 2 == 0:
        locationsA.append(input[number])
    
    else:
        locationsB.append(input[number])

locationsA.sort()
locationsB.sort()

similarityScore = 0

for locationA in locationsA:
    locationCount = 0

    for locationB in locationsB:
        if locationA == locationB: locationCount += 1
    
    similarityScore += locationA * locationCount

print(similarityScore)