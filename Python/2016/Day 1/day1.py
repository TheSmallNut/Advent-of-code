import os
import sys

def findCoordinates(splitString):
    direction = 0
    x = 0
    y = 0
    for i in splitString:
        number = int(i[1])
        rotation = i[0]
        if(rotation == "R"):
            direction += 1
        elif(rotation == "L"):
            direction -= 1
        if(direction <= -1):
            direction = 3
        elif(direction >= 4):
            direction = 0
        if(direction == 0):
            y += number
        elif(direction == 1):
            x += number
        elif(direction == 2):
            y -= number
        elif(direction == 3):
            x -= number
    print(x)
    print(y)


def splitArray(string):
    splitString = string.split(" ")
    for i in range(0, len(splitString)):
        splitString[i] = splitString[i][0:2]
    return splitString

if __name__ == "__main__":
    path = os.path.join(sys.path[0], 'input.txt')
    test = open(path)
    content = test.read()
    test.close()
    findCoordinates(splitArray(content))
