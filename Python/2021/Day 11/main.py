import os
import sys


path = os.path.join(sys.path[0], 'input.txt')
file = open(path)
lines = file.readlines()
file.close()

octopies = []


def flashOctopus(octopus):
    toCheck = [[-1, -1], [0, -1], [1, -1],
               [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
    if octopus[0] == 0:
        toCheck.pop([-1, -1])
        toCheck.pop([-1, 0])
        toCheck.pop([-1, 1])
    if octopus[1] == 0:
        None


def addOctopie():
    list = []
    y = 0
    for line in lines:
        x = 0
        for letter in line:
            list.append([x, y])
            x += 1
        y += 1
    return list


octopies = addOctopie()
