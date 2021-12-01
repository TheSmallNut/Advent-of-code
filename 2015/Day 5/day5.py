import os
import sys

VOWELS = ["a", "e", "i", "o", "u"]
EVILSTRINGS = ["ab", "cd", "pq", "xy"]


# returns true if there is a duplicate in the line

def lineContainsDuplicate(line):
    for i in range(len(line) - 1):
        if line[i] == line[i+1]:
            return True
    return False

# gives amount of vowels in the line


def vowelsIn(line):
    totalVowels = 0
    for letter in line:
        for vowel in VOWELS:
            if vowel == letter:
                totalVowels += 1
    return totalVowels


# If it contains an evil string, returns true
def containsEvilStrings(line):
    for i in range(len(line) - 1):
        for string in EVILSTRINGS:
            if line[i] + line[i+1] == string:
                return True
    return False


# FUNCTION

path = os.path.join(sys.path[0], 'input.txt')
test = open(path)
content = test.read()
test.close()
content_lines = content.splitlines()
total = 0
for line in content_lines:
    if vowelsIn(line) < 3:
        continue
    if containsEvilStrings(line):
        continue
    if not lineContainsDuplicate(line):
        continue
    total += 1
print(total)
