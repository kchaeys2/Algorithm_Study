from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())

for _ in range(N):
    a, b = map(int,stdin.readline().split())
    queP = deque(map(int, stdin.readline().split()))

    result = 0

    while queP:
        if b<0:
            break
        elif queP[0] == max(queP):
            b-=1
            result+=1
            queP.popleft()
        else:
            if b==0:
                queP.rotate(-1)
                b = len(queP)-1
            else:
                queP.rotate(-1)
                b-=1
    
    print(result)