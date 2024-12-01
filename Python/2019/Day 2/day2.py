import os
import sys
import math

def calculate(content, startingPos):
    number = 0
    if content[startingPos] == 1:
        number = content[startingPos+1] + content[startingPos+2]
    elif content[startingPos] == 2:
        number = content[startingPos+1] * content[startingPos+2]
    content[content[startingPos+3]] = number
    return content

if __name__ == "__main__":
    path = os.path.join(sys.path[0], 'input.txt')
    test = open(path)
    content = test.read()
    content = content.split(",")
    for i in range(0,len(content)):
        content[i] = int(content[i])
    content[1] = 12
    content[2] = 2
    i=0
    while(True):
        print(content)
        if content[i] == 99:
            break
        content = calculate(content,i)
        i += 4
    print(content)
