import os
import sys


path = os.path.join(sys.path[0], 'input.txt')
test = open(path)
content = test.read()
test.close()
numbers = content.splitlines()


def something():
    current = 0
    listOfFrequencies = [0]
    while True:
        for number in numbers:
            current += int(number)
            if int(current) in list(listOfFrequencies):
                print(current)
                return
            listOfFrequencies.append(int(current))


something()
# print(current)
