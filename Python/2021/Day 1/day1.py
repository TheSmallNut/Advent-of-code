import os, sys    
path = os.path.join(sys.path[0], 'input.txt')
file = open(path)
lines = file.read().split("\n")
file.close()


previousNumber = int(lines[0])
previousWindow = int(lines[0]) + int(lines[1]) + int(lines[2])
totalIncreases = 0

# for number in lines:
#     if int(number) > previousNumber:
#         totalIncreases += 1
#     previousNumber = int(number)

for x in range(len(lines) - 2):
    window = int(lines[x]) + int(lines[x + 1]) + int(lines[x + 2])
    if window > previousWindow:
        totalIncreases += 1
    previousWindow = window

print(totalIncreases)