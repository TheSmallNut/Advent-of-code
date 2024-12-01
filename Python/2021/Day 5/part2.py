import os
import sys


path = os.path.join(sys.path[0], 'input.txt')
file = open(path)
lines = file.readlines()
file.close()


coords = []
overlap = 0

def isNegative(number):
    if number < 0:
        return True

def addCoordinates(x, y):
    global overlap
    coordinate = [int(x), int(y)]
    count = coords.count(coordinate)
    if count == 1:
        overlap += 1
    coords.append(coordinate)

def areXEquals(x1, y1, x2, y2):
    if x1 == x2:
        return True
    elif y1 == y2:
        return False
    else:
        return None


for line in lines:
    line = line.split()
    coordinatesOne = line[0].split(",")
    coordinatesTwo = line[2].split(",")
    x1 = int(coordinatesOne[0])
    y1 = int(coordinatesOne[1])
    x2 = int(coordinatesTwo[0])
    y2 = int(coordinatesTwo[1])
    xEquals = areXEquals(x1, y1, x2, y2)
    if xEquals == None:
        for i in range(abs(x1 - x2) + 1):
            x = x1
            y = y1
            if isNegative(x1 - x2):
                x += i
            else:
                x -= i
            
            if isNegative(y1 - y2):
                y += i
            else:
                y -= i
            addCoordinates(x, y)
    elif xEquals == True:
        for i in range(abs(y1 - y2) + 1):
            x = x1
            y = min(y1, y2) + i
            addCoordinates(x, y)
    elif xEquals == False:
        for i in range(abs(x1 - x2) + 1):
            x = min(x1, x2) + i
            y = y1
            addCoordinates(x, y)

print(overlap)
