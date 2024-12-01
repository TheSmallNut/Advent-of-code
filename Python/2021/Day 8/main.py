import os
import sys


path = os.path.join(sys.path[0], 'input.txt')
file = open(path)
lines = file.readlines()
file.close()

outputs = []

for line in lines:
    split = line.split("|")
    output = split[1].strip()
    for segment in output.split(" "):
        outputs.append(segment)

total1478 = 0
CHECK_FOR_DIGITS = [2, 3, 4, 7]
for output in outputs:
    if len(output) in CHECK_FOR_DIGITS:
        total1478 += 1
print(total1478)
