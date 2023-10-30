from sys import stdin
from collections import deque

N,M = map(int,stdin.readline().split())
visit = [[False]*M for _ in range(N)]
res = [[-1]*M for _ in range(N)]
direction = [(-1,0),(1,0),(0,1),(0,-1)]
que = deque([])

road = []
for n in range(N):
    tempR = list(map(int,stdin.readline().split()))
    for m in range(M):
        if tempR[m] == 2:
             que.append((n,m))
             visit[n][m] = True
             res[n][m] = 0
        elif tempR[m] == 0:
             res[n][m] = 0
    road.append(tempR)
while que:
    px,py = que.popleft()
    
    for dx,dy in direction:
        tempx,tempy = px+dx,py+dy
        
        if -1< tempx < N and -1 < tempy < M and not visit[tempx][tempy] and road[tempx][tempy] == 1:
            res[tempx][tempy] = res[px][py] + 1
            visit[tempx][tempy] = True
            que.append((tempx,tempy))

for row in res:
    for line in row:
        print(line,end=" ")
    print()
            
