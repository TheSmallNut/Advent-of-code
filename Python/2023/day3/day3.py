import os
import requests
from dotenv import load_dotenv

load_dotenv()
day = 3
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