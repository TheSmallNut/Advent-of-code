import os
import sys

def checkPassword(min,max,letter,words):
    numberOfLetter = words.count(letter)
    if numberOfLetter >= min and numberOfLetter <= max:
        return True
    else:
        return False
def checkPasswordPolicy(test_list):
    correctPasswords = 0
    for line in test_list:
        x = line.split(" ")
        num = x[0].split("-")
        letter = x[1][0]
        if checkPassword(int(num[0]), int(num[1]), letter, x[2]):
            correctPasswords +=1
    print(correctPasswords)

def checkPositions(test_list):
    correctPasswords = 0
    for line in test_list:
        x = line.split(" ")
        num = x[0].split("-")
        letter = x[1][0]
        for i in range(0, len(num)):
            num[i] = int(num[i])

        if (x[2][num[0]-1] == letter) ^ (x[2][num[1]-1] == letter):
            correctPasswords +=1

    print(correctPasswords)


if __name__ == "__main__":
    path = os.path.join(sys.path[0], 'input.txt')
    test = open(path)
    testContent = test.read()
    test_list = testContent.splitlines()
    test.close()
    checkPasswordPolicy(test_list)
    checkPositions(test_list)
