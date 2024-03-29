import os
import sys


path = os.path.join(sys.path[0], 'input.txt')
file = open(path)
input = file.readlines()
file.close()


listOfLists = []
oxygenGeneratorValue = list(listOfLists)

for line in input:
    line = line.split()[0]
    if len(listOfLists) != len(line):
        for number in line:
            listOfLists.append([])

    for x in range(len(line)):
        listOfLists[x].append(int(line[x]))


def getMostCommonNumberInList(list):
    zero_count = list.count(0)
    one_count = list.count(1)
    if zero_count > one_count:
        return 0
    elif one_count > zero_count:
        return 1
    elif one_count == zero_count:
        return None


mostCommonNumberList = []
leastCommonNumberList = []
for list in listOfLists:
    mostCommonNumber = getMostCommonNumberInList(list)
    if mostCommonNumber == None:
        mostCommonNumber = 1
    leastCommonNumber = abs(mostCommonNumber - 1)
    mostCommonNumberList.append(mostCommonNumber)
    leastCommonNumberList.append(leastCommonNumber)


def oxygenGeneratorValue():
    for list in listOfLists:
        for x in range(len(list)):
            index = (listOfLists.index(list))
            print(index)
            if list[x] != mostCommonNumberList[index]:
                listOfLists.remove(list)


oxygenGeneratorValue()
# print(listOfLists)
