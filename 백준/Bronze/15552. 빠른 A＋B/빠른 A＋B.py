import sys
count = int(sys.stdin.readline())
plusList = []
for i in range(count):
    A,B = map(int,sys.stdin.readline().split())
    plusList.append(A+B)
for plus in plusList:
    print(plus)