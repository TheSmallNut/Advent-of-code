import time
with open('./2023/day1/input.txt', 'r') as file:
    # Read the contents of the file
    contents = file.readlines()


def run():
    total = 0
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    numbersDict = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
    }

    for line in contents:
        nums = []
        for letteredNumber in numbersDict:
            line = line.replace(letteredNumber, (numbersDict[letteredNumber]))
        for letter in line:
            if letter in numbers:
                nums.append(letter)
        num = nums[0] + nums[-1]
        total += int(num)


startTime = time.time()
for i in range(1000):
    run()
endTime = time.time()

totalTime = endTime - startTime

print(totalTime)