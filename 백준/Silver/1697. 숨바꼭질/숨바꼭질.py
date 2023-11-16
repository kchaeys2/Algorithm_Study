from sys import stdin
from collections import deque

N,K = map(int,stdin.readline().split())

pointTime = [0]*100001

def bfs(n):
    que = deque([n])
    while que:
        point = que.popleft()
        if point == K:
            return pointTime[K]
        for p in (point+1,point*2,point-1):
            if 0<= p < 100001 and not pointTime[p]:
                pointTime[p] = pointTime[point] + 1
                que.append(p)

print(bfs(N))