input_file_path = f"Python/2024/day1/input.txt"

with open(input_file_path, 'r') as file:
    contents = [line.strip() for line in file.readlines()]

leftList = []
rightList = []


for line in contents:
    nums = line.split("   ")
    leftList.append(int(nums[0]))
    rightList.append(int(nums[1]))

leftList.sort()
rightList.sort()

total = 0
for i in range(len(leftList)):
    total += abs(leftList[i] - rightList[i])
