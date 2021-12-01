import os
import sys


path = os.path.join(sys.path[0], 'input.txt')
test = open(path)
content = test.read()
test.close()
lines = content.splitlines()
numbers = []
for line in lines:
    numbers = line.split("\t")
    greatest = int(numbers[0])
    least = int(numbers[0])
    for number in numbers:
        if int(number) > greatest:
            greatest = int(number)
        if int(number) < least:
            least = int(number)
    numbers.append(int(greatest - least))
total = 0
for number in numbers:
    total += int(number)
print(total)
