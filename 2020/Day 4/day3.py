import os
import sys

requiredPassportFields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
currentIndex = 0

def checkPassport(startingIndex, list):
    variables = getVariablesIntoList(startingIndex, list)
    for field in requiredPassportFields:
        valid = False
        for variable in variables:
            if field in variable:
                valid = True
                break
        if valid == False:
            return False
    return True

def getVariablesIntoList(startingIndex,list):
    i = 0
    endingIndex = 0
    while(True):
        if list[i+startingIndex] == "\n":
            endingIndex = i+startingIndex
            break
        elif startingIndex+i == len(list)-1:
            endingIndex = len(list)
            break
        i += 1
    variables = []
    for i in range(0, endingIndex - startingIndex):
        lineList = list[i+startingIndex].split(" ")
        for i in lineList:
            variables.append(i)
    global currentIndex
    currentIndex = endingIndex + 1
    return variables

if __name__ == "__main__":
    path = os.path.join(sys.path[0], 'input.txt')
    input = open(path)
    path = os.path.join(sys.path[0],'testInput.txt')
    test = open(path)
    list = input.readlines()
    test_list = test.readlines()
    validPassports = 0
    while(True):
        if currentIndex >= len(list):
            break
        if checkPassport(currentIndex,list):
            validPassports += 1
    print(validPassports)
