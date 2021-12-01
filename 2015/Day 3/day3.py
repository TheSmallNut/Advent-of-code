import os
import sys


def addCoordinate(currentCoordinate, listOfCoordinates):
    for coordinate in listOfCoordinates:
        if currentCoordinate == coordinate:
            return
    listOfCoordinates.append(list(currentCoordinate))
    return listOfCoordinates


def move(symbol, coordinate):
    if symbol == ">":
        coordinate[0] += 1
    elif symbol == "<":
        coordinate[0] -= 1
    elif symbol == "^":
        coordinate[1] += 1
    elif symbol == "v":
        coordinate[1] -= 1


path = os.path.join(sys.path[0], 'input.txt')
test = open(path)
content = test.read()
test.close()
currentCoordinate = [0, 0]
listOfCoordinates = [list(currentCoordinate)]
for symbol in content:
    move(symbol, currentCoordinate)
    addCoordinate(currentCoordinate, listOfCoordinates)
print(len(listOfCoordinates))
