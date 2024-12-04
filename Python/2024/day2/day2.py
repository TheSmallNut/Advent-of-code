

input_file_path = f"Python/2024/day2/input.txt"

with open(input_file_path, 'r') as file:
    contents = [line.strip() for line in file.readlines()]


def checkLine(numbers):
    increasingOrDecreasing = 0
    for i in range(len(numbers) - 1):
        if i == len(numbers):
            return
        num1 = int(numbers[i])
        num2 = int(numbers[i+1])
        if increasingOrDecreasing == 0:
            if num1 - num2 > 0:
                increasingOrDecreasing = 1
            else:
                increasingOrDecreasing = -1
        elif increasingOrDecreasing == 1:
            if num1 - num2 < 0:
                return False
        elif increasingOrDecreasing == -1:
            if num1 - num2 > 0:
                return False


        if abs(num1 - num2) > 3:
            return False
        if num1 == num2:
            return False
    return True

totalSafe = 0
for line in contents:
    numbers = line.split(" ")
    print(checkLine(numbers))
    if checkLine(numbers):
        totalSafe += 1
print(totalSafe)