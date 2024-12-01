import os
import sys


path = os.path.join(sys.path[0], 'input.txt')
file = open(path)
lines = file.readlines()
file.close()


numberList = []


def checkUp(x, y):
    try:
        if y == 0:
            raise
        return numberList[y][x] < numberList[y - 1][x]
    except:
        return True


def checkDown(x, y):
    try:
        if y == len(numberList)-1:
            raise
        return numberList[y][x] < numberList[y + 1][x]
    except:
        return True


def checkRight(x, y):
    try:
        if x == len(numberList[y]):
            raise
        return numberList[y][x] < numberList[y][x + 1]
    except:
        return True


def checkLeft(x, y):
    try:
        if x == 0:
            raise
        return numberList[y][x] < numberList[y][x - 1]
    except:
        return True

# Returns true if everything around it is larger than it


def checkAroundCoordinate(x, y):
    right = (checkRight(x, y))
    left = (checkLeft(x, y))
    up = (checkUp(x, y))
    down = (checkDown(x, y))
    return (right and left and up and down)


for line in lines:
    line = line.strip()
    numberList.append([])
    for num in line:
        numberList[-1].append(int(num))

total = 0
nums = []
for y in range(len(numberList)):
    for x in range(len(numberList[y])):
        if checkAroundCoordinate(x, y):
            nums.append(numberList[y][x] + 1)
            total += 1
print(total)
print(nums)
print(sum(nums))
