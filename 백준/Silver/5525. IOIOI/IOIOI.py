from sys import stdin
N = int(stdin.readline().rstrip())
M = int(stdin.readline().rstrip())
S = stdin.readline().rstrip()

cnt=0
res = 0
for s in S:
    if s == "O" and cnt%2==1:
        cnt+=1
    elif s == "I" and cnt%2 == 0:
        cnt+=1
    elif s == "I":
        cnt = 1
    else:
        cnt = 0
    if cnt >= 1+2*N and cnt%2==1:
        res+=1

print(res)