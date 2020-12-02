import os
import sys

if __name__ == "__main__":
    path = os.path.join(sys.path[0], 'input.txt')
    test = open(path)
    testContent = test.read()
    test_list = testContent.splitlines()
    test.close()
    print(test_list)
    print("\n")
