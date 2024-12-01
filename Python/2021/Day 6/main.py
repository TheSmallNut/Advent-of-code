import os
import sys


path = os.path.join(sys.path[0], 'input.txt')
file = open(path)
numberFile = file.read()
file.close()
NUMBER_OF_DAYS = 256

fishList = [int(i) for i in numberFile.split(",")]


newFish = []

for i in range(NUMBER_OF_DAYS):
    for x in range(len(fishList)):
        if fishList[x] == 0:
            newFish.append(8)
            fishList[x] = 6
        else:
            fishList[x] -= 1
    fishList = fishList + newFish
    newFish = []
    print(f"Ran Day {i}")


print(len(fishList))
