import os, sys    
path = os.path.join(sys.path[0], 'input.txt')
file = open(path)
lines = file.readlines()
file.close()


horizontalPosition = 0
depth = 0
aim = 0
for line in lines:
    line = line.split()
    if line[0] == "forward":
        horizontalPosition += int(line[1])
        depth += aim * int(line[1])
    elif line[0] == "down":
        aim += int(line[1])
    elif line[0] == "up":
        aim -= int(line[1])

print(horizontalPosition * depth)
    
