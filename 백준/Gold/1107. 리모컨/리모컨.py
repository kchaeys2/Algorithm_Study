from sys import stdin

N = int(stdin.readline().rstrip())
M = int(stdin.readline().rstrip())
notBtn = list(stdin.readline().split())

minCnt = abs(100 - N)

for i in range(1000000):
    num = str(i)
    length = len(num)
    for n in range(length):
        if num[n] in notBtn:
            break
        if n == length-1:
            minCnt = min(minCnt,abs(i-N)+length)
print(minCnt)