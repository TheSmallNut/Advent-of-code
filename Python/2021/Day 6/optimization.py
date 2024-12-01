import os
import sys


path = os.path.join(sys.path[0], 'input.txt')
file = open(path)
numberFile = file.read()
file.close()
NUMBER_OF_DAYS = 256

fishList = [int(i) for i in numberFile.split(",")]
totalFish = [0, 0, 0, 0, 0, 0, 0, 0, 0]


for fish in fishList:
    totalFish[fish] += 1

for i in range(NUMBER_OF_DAYS):
    tempList = list(totalFish)
    totalFish[0] = tempList[1]
    totalFish[1] = tempList[2]
    totalFish[2] = tempList[3]
    totalFish[3] = tempList[4]
    totalFish[4] = tempList[5]
    totalFish[5] = tempList[6]
    totalFish[6] = tempList[7] + tempList[0]
    totalFish[7] = tempList[8]
    totalFish[8] = tempList[0]


print(sum(totalFish))
