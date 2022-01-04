import os
import sys


path = os.path.join(sys.path[0], 'input.txt')
file = open(path)
bigFile = file.read()
file.close()

bigFile = bigFile.split("\n\n")
dots = bigFile[0].split("\n")
instructions = bigFile[1].split("\n")

listOfDots = []
for dot in dots:
    dot = dot.split(",")
    listOfDots.append([int(dot[0]), int(dot[1])])
