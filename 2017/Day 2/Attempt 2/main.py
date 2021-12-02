import os
import sys


path = os.path.join(sys.path[0], 'input.txt')
file = open(path)
lines = file.readlines()
file.close()


integerList = []
for line in lines:
    line = line.split()
    integerList.append(list(map(int, line)))

# totalNumbers = []
# for line in integerList:
#     greatestNumberInLine = line[0]
#     smallestNumberInLine = line[0]
#     for number in line:
#         greatestNumberInLine = max(number, greatestNumberInLine)
#         smallestNumberInLine = min(number, smallestNumberInLine)
#     totalNumbers.append(greatestNumberInLine - smallestNumberInLine)

# print(sum(totalNumbers))

totalNumbers = []
for line in integerList:
    for x in range(len(line)):
        for z in range(x + 1, len(line)):
            if line[x] % line[z] == 0:
                totalNumbers.append(int(line[x] / line[z]))
            elif line[z] % line[x] == 0:
                totalNumbers.append(int(line[z] / line[x]))

print(sum(totalNumbers))
