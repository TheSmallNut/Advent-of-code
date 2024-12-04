import re
input_file_path = f"Python/2024/day3/input.txt"

with open(input_file_path, 'r') as file:
    contents = file.read()

pattern = r'mul\(\d+,\s*\d+\)'


matches = re.findall(pattern, contents)

total = 0
for match in matches:
    numbers = match[4:][:-1].split(",")
    total += int(numbers[0]) * int(numbers[1])

print(total)

