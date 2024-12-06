import os

inputFile = "Day 4 Input.txt"

scriptDir = os.path.dirname(__file__)
inputFile = os.path.join(scriptDir, inputFile)

input = []

with open(inputFile, "r") as file:
    for line in file:
        row = []

        for character in line:
            if character != "\n":
                row.append(character)

        input.append(row)

directions = [
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1)

]

wordToFind = "XMAS"
wordLetters = []

for letter in wordToFind:
    wordLetters.append(letter)

occurences = 0

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
                occurences += 1

print(occurences)