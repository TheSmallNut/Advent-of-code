import itertools

def say_two (content_list):
    for a,b in itertools.combinations(content_list,2):
        if a + b == 2020:
            print(a)
            print(b)
def  say_three(content_list):
    for a,b,c in itertools.combinations(content_list,3):
        if a + b + c == 2020:
            print(a)
            print(b)
            print(c)
if __name__ == "__main__":
    test = open(r'C:\Users\James\Desktop\Code\Advent of code\Day 1\mytext.txt')
    testContent = test.read()
    test_list = testContent.splitlines()
    test.close()
    for i in range(0, len(test_list)):
        test_list[i] = int(test_list[i])
    say_two(test_list)
    print("\n")
    say_three(test_list)
#for x in range(0, len(content_list)):
#    for i in range(0, len(content_list)):
#        answer = (content_list[i] + content_list[x])
#        if answer ==  2020:
#            content_list[i]
#            content_list[x]
