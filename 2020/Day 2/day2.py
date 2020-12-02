import os
import sys

def checkPassword(min,max,letter,words):
    numberOfLetter = words.count(letter)
    if numberOfLetter >= min and numberOfLetter <= max:
        return True
    else:
        return False


if __name__ == "__main__":
    path = os.path.join(sys.path[0], 'input.txt')
    test = open(path)
    testContent = test.read()
    test_list = testContent.splitlines()
    test.close()
    correctPasswords = 0
    incorrectPasswords = 0
    for line in test_list:
        x = line.split(" ")
        num = x[0].split("-")
        letter = x[1]
        if checkPassword(int(num[0]), int(num[1]), letter[0], x[2]):
            correctPasswords +=1
        else:
            incorrectPasswords+=1
    print(correctPasswords)
