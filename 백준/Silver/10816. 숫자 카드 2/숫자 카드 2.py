from sys import stdin

_ = int(stdin.readline())
N = list(map(int, stdin.readline().split()))
_ = int(stdin.readline())
M = list(map(int, stdin.readline().split()))

dict = {}
for n in N:
    if n in dict:
        dict[n]+=1
    else:
        dict[n] = 1
for target in M:
    result = dict.get(target)
    
    if result == None:
        print(0,end=" ")
    else:
        print(result,end=" ")
