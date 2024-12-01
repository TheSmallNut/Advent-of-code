import os
import sys
import math

def sumUpAllFuel(list):
    fuel = 0
    for i in list:
        mass = i
        while(True):
            fuelRequired = math.floor(int(mass)/3) - 2
            if fuelRequired <= 0:
                break
            fuel += fuelRequired
            mass = fuelRequired
    return fuel


if __name__ == "__main__":
    path = os.path.join(sys.path[0], 'input.txt')
    test = open(path)
    list = test.readlines()
    print(sumUpAllFuel(list))
