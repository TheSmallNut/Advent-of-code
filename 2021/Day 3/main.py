import os
import sys


path = os.path.join(sys.path[0], 'input.txt')
file = open(path)
input = file.readlines()
file.close()




listOfLists = []

for line in input:
    line = line.split()[0]
    if len(listOfLists) != len(line):
        for number in line:
            listOfLists.append([])

    for x in range(len(line)):
        listOfLists[x].append(int(line[x]))


mostCommonNumber = ""
leastCommonNumber = ""
for list in listOfLists:
    zero = 0
    one = 0
    for num in list:
        if num == 0:
            zero += 1
        elif num == 1:
            one += 1
    if max(zero, one) == zero:
        mostCommonNumber += "0"
        leastCommonNumber += "1"
    elif max(zero, one) == one:
        mostCommonNumber += "1"
        leastCommonNumber += "0"

decimalMostCommon = int(mostCommonNumber, 2)
decimalLeastCommon = int(leastCommonNumber, 2)

print(decimalMostCommon * decimalLeastCommon)

    




