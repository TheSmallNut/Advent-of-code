import os
import sys


path = os.path.join(sys.path[0], 'input.txt')
file = open(path)
lines = file.read()
file.close()
bingoBoards = lines.split("\n\n")

listOfBoards = []
drawNumbers = bingoBoards.pop(0)


def checkIfWinner(board):
    for line in board:
        if line.count(True) == 5:
            return True


for line in bingoBoards:
    listOfBoards.append([])
    lines = line.split("\n")
    for differentLine in lines:
        listOfBoards[-1].append([])
        for num in differentLine.split():
            listOfBoards[-1][-1].append(int(num))

for board in listOfBoards:
    print(board)
