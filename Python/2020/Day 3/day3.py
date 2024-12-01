import os
import sys

def checkForTree(x,y,test_list):
    return test_list[y][x] == "#"

def slopeQuestion(changeX, changeY, test_list):
    x = 0
    y = 0
    trees = 0
    for i in range(0, len(test_list)-1):
        x += changeX
        x %= len(test_list[i])-1
        y += changeY
        if y >= len(test_list):
            break
        if checkForTree(x,y,test_list):
            trees+= 1
    return trees

if __name__ == "__main__":
    path = os.path.join(sys.path[0], 'input.txt')
    test = open(path)
    test_list = test.readlines()
    totalTrees = slopeQuestion(1,1,test_list) * slopeQuestion(3, 1, test_list) * slopeQuestion(5, 1, test_list) * slopeQuestion(7, 1, test_list) * slopeQuestion(1, 2, test_list)
    print(totalTrees)
