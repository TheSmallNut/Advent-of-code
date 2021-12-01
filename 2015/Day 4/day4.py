import os
import sys
import hashlib

startingInput = "iwrupvqb"
i = 0
while True:
    i += 1
    input = startingInput + str(i)
    hash_object = hashlib.md5(input.encode())
    md5_hash = hash_object.hexdigest()
    if md5_hash[0:7] == "0000000":
        print(i)
        print(input)
        print(md5_hash)
        break
