import os, sys    
path = os.path.join(sys.path[0], 'input.txt')
file = open(path)
lines = file.readlines()
file.close()



twoLetters = 0
threeLetters = 0

for line in lines:
    hasTwoLettered = False
    hasThreeLettered = False
    line = line.strip()
    soloLetters = []
    for letter in line:
        if letter not in soloLetters:
            soloLetters.append(letter)
    for soloLetter in soloLetters:
        count = line.count(soloLetter)
        if count == 2:
            if not hasTwoLettered:
                twoLetters += 1
                hasTwoLettered = True
        elif count == 3:
            if not hasThreeLettered:
                threeLetters += 1
                hasThreeLettered = True


print(twoLetters * threeLetters)
        


