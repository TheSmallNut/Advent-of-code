import os
import sys


def addCoordinate(currentCoordinate, listOfCoordinates):
    for coordinate in listOfCoordinates:
        if currentCoordinate == coordinate:
            return
    listOfCoordinates.append(list(currentCoordinate))


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

turn = True

# starting Coordinate
santaCoordinate = [0, 0]

visitedHouses = [list(santaCoordinate)]

# starting Coordinate
roboCoordinate = [0, 0]

for symbol in content:
    if turn == True:
        turn = False
        move(symbol, santaCoordinate)
        addCoordinate(santaCoordinate, visitedHouses)
    elif turn == False:
        turn = True
        move(symbol, roboCoordinate)
        addCoordinate(roboCoordinate, visitedHouses)
print(len(visitedHouses))
print(visitedHouses)
