import os
import sys
import math

def paperCalculator(content_list):
    totalPaper = 0
    for equation in content_list:
        numbers = equation.split("x")
        for i in range(0, len(numbers)):
            numbers[i] = int(numbers[i])
        length = numbers[0]
        width = numbers[1]
        height = numbers[2]
        side1 = length * width * 2
        side2 = width * height * 2
        side3 = height * length * 2
        areaOfSmallestSide = (min(side1,side2,side3))/2
        totalPaper += areaOfSmallestSide + side1 + side2 + side3
    return math.floor(totalPaper)
def ribbonCalculator(content_list):
    totalRibbon = 0
    for equation in content_list:
        numbers = equation.split("x")
        for i in range(0, len(numbers)):
            numbers[i] = int(numbers[i])
        length = numbers[0]
        width = numbers[1]
        height = numbers[2]
        totalRibbon += length * width * height
        largest = max(length,width,height)
        smallest = min(length,width,height)
        middle = length+width+height - smallest - largest
        totalRibbon += (smallest*2) + (middle * 2)
    return totalRibbon





if __name__ == "__main__":
    path = os.path.join(sys.path[0], 'input.txt')
    test = open(path)
    content = test.read()
    test.close()
    content_lines = content.splitlines()
    print(paperCalculator(content_lines))
    print(ribbonCalculator(content_lines))
