import os
import sys

if __name__ == "__main__":
    path = os.path.join(sys.path[0], 'input.txt')
    test = open(path)
    content = test.read()
    print(content)
    test.close()
    floor = 0
    reachedFloor = False
    length = 0
    for i in content:
        length += 1
        if i == "(":
            floor += 1
        elif i == ")":
            floor -= 1
            if not reachedFloor and floor == -1:
                print(length)
    print(floor)
