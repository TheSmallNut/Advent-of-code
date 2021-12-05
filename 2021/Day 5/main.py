import os
import sys


path = os.path.join(sys.path[0], 'input.txt')
file = open(path)
lines = file.readlines()
file.close()

coordinatesTaken = []

overlaps = 0


def addCoordinates(x, y):
    global overlaps
    coordinate = [int(x), int(y)]
    if coordinatesTaken.count(coordinate) == 1:
        overlaps += 1
    coordinatesTaken.append(coordinate)
    

consideredLines = []
for line in lines:
    splitLine = line.split(" ")
    coordinateOne = splitLine[0].split(",")
    coordinateTwo = splitLine[2].split(",")
    x1 = coordinateOne[0].strip()
    x2 = coordinateTwo[0].strip()
    y1 = coordinateOne[1].strip()
    y2 = coordinateTwo[1].strip()

    if x1 == x2 or y1 == y2:
        consideredLines.append(line.strip())

print(consideredLines)

for line in consideredLines:
    splitLine = line.split(" ")
    coordinateOne = splitLine[0].split(",")
    coordinateTwo = splitLine[2].split(",")
    x1 = int(coordinateOne[0].strip())
    x2 = int(coordinateTwo[0].strip())
    y1 = int(coordinateOne[1].strip())
    y2 = int(coordinateTwo[1].strip())

    if x1 == x2:
        for i in range(abs(y1 - y2) + 1):
            addCoordinates(x1, min(y1, y2) + i)
    elif y1 == y2:
        for i in range(abs(x1 - x2) + 1):
            addCoordinates(min(x1, x2) + i, y1)

print(overlaps)
    

