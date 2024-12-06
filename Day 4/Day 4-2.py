import os

inputFile = "Day 4 Input.txt"

scriptDir = os.path.dirname(__file__)
inputFile = os.path.join(scriptDir, inputFile)

input = []

with open(inputFile) as file:
    for line in file:
        row = []

        for character in line:
            if character != "\n":
                row.append(character)
        
        input.append(row)

directions = [
    (1, 1),
    (1, -1),
    (-1, -1),
    (-1, 1)

]

wordToFind = "MAS"
wordLetters = []

for letter in wordToFind:
    wordLetters.append(letter)

occurances = 0
aCoordinates = []

for row in range(len(input)):
    for square in range(len(input[row])):
        for direction in directions:
            directionSolved = True

            for letterIndex in range(len(wordLetters)):
                horizontalChange = direction[0]
                verticalChange = direction[1]

                horizontal = square + (letterIndex * horizontalChange)
                vertical = row + (letterIndex * verticalChange)

                if (vertical < 0 or vertical >= len(input)) or (horizontal < 0 or horizontal >= len(input[row])):
                    directionSolved = False
                    break

                elif input[vertical][horizontal] != wordLetters[letterIndex]:
                    directionSolved = False
                    break
            
            if directionSolved:
                occurances += 1
                aCoordinate = (square + direction[0], row + direction[1])
                aCoordinates.append(aCoordinate)

crossLedger = {}
totalCrosses = 0

for coordinate in aCoordinates:
    if coordinate in crossLedger:
        crossLedger[coordinate] += 1
    
    else:
        crossLedger[coordinate] = 1
    
for count in crossLedger.values():
    if count > 1:
        totalCrosses += 1

print(totalCrosses)