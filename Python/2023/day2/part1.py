import os
import requests
from dotenv import load_dotenv

load_dotenv()
day = 2
url = f"https://adventofcode.com/2023/day/{day}/input"
input_file_path = f"2023/day{day}/input.txt"

# Check if the input file already exists
if not os.path.exists(input_file_path):
    COOKIE = os.getenv('COOKIE')
    headers = {
        "Cookie": f"session={COOKIE}"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        with open(input_file_path, "w") as file:
            contents = response.text.splitlines()
            file.write(response.text)
        print("Input file downloaded successfully.")
    else:
        print(f"Failed to download input file. Status code: {response.status_code}")
else:
    with open(input_file_path, 'r') as file:
        contents = [line.strip() for line in file.readlines()]

MAX_COLORS = {"red" : 12, "green" : 13, "blue" : 14}
passedIDs = []
for game in contents:
    gameSplit = game.split(":")
    rounds = gameSplit[1].split(";")
    passed = True
    for roll in rounds:
        colors = roll.split(",")
        for color in colors:
            number = color.split(" ")
            if int(number[1]) > MAX_COLORS[number[2]]:
                passed = False
                break
        if not passed:
            break
    if not passed:
        continue
    passedIDs.append(gameSplit[0].split(" ")[-1])

total = 0
for id in passedIDs:
    total += int(id)

print(total)


