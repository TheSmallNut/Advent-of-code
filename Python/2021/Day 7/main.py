import os
import sys


path = os.path.join(sys.path[0], 'input.txt')
file = open(path)
bigFile = file.read()
file.close()

stringNumbers = bigFile.split(",")
numbers = []

for number in stringNumbers:
    numbers.append(int(number))

bestFuelCost = None
bestNumberToBeAt = None
for i in range(max(numbers)):
    fuelCost = 0
    for number in numbers:
        for x in range(abs(i - number) + 1):
            fuelCost += x
    if bestFuelCost == None:
        bestFuelCost = fuelCost
        bestNumberToBeAt = i
    elif fuelCost < bestFuelCost:
        bestFuelCost = fuelCost
        bestNumberToBeAt = i

print(f"best Fuel Cost: {bestFuelCost} | Number: {bestNumberToBeAt}")
