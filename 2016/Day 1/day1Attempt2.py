import os
import sys


path = os.path.join(sys.path[0], 'input.txt')
test = open(path)
content = test.read()
test.close()

splitContent = content.split(", ")


location = [0, 0]
currentDirection = "N"
directions = ["N", "E", "S", "W"]
locationList = [list(location)]


def setCurrentDirection(direction):
    global currentDirection
    if direction == "R":
        for i in range(len(directions)):
            if currentDirection == directions[i]:
                if directions[i] == "W":
                    currentDirection = "N"
                else:
                    currentDirection = str(directions[i+1])
                return
    elif direction == "L":
        for i in range(len(directions)):
            if currentDirection == directions[i]:
                if currentDirection == "N":
                    currentDirection = "W"
                else:
                    currentDirection = str(directions[i-1])
                return


def move(length):

    global currentDirection
    if currentDirection == "N":
        location[1] += length
    elif currentDirection == "S":
        location[1] -= length
    elif currentDirection == "E":
        location[0] += length
    elif currentDirection == "W":
        location[0] -= length


for movement in splitContent:
    setCurrentDirection(movement[0])
    move(int(movement[1:]))
    if location in locationList:
        print(location)
    locationList.append(list(location))
