import os

inputFile = "Day 3 Input.txt"

script_dir = os.path.dirname(__file__)
inputFile = os.path.join(script_dir, inputFile)

input = ""
numbers = "1234567890"

with open(inputFile, 'r') as file:
    for line in file:
        input += line

mulIndexes = [i for i in range(len(input)) if input.startswith("mul(", i)]

totalSum = 0

for attemptIndex in mulIndexes:
    number1 = []
    number2 = []

    characterTry = ""

    hasReachedFlag = False
    isDeadAttempt = False

    for attempt in range(4):
        characterTry = input[attemptIndex + 4 + attempt]

        if characterTry in numbers:
            number1.append(characterTry)
        
        elif characterTry == ",":
            hasReachedFlag = True

            break

        else:
            isDeadAttempt = True
    
    if isDeadAttempt or not hasReachedFlag: continue

    for attempt in range(4):
        characterTry = input[attemptIndex + 4 + len(number1) + 1 + attempt]

        if characterTry in numbers:
            number2.append(characterTry)
        
        elif characterTry == ")":
            hasReachedFlag = True

            break

        else:
            isDeadAttempt = True
    
    if isDeadAttempt or not hasReachedFlag: continue

    finalNumber1 = int("".join(number1))
    finalNumber2 = int("".join(number2))

    #print(finalNumber1)
    #print(finalNumber2)

    totalSum += (finalNumber1 * finalNumber2)

print(totalSum)