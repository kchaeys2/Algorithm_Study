from sys import stdin
from collections import deque

N,M = map(int,stdin.readline().split())
campus = []
visit = [[False]*M for _ in range(N)]
startX,startY = 0,0
for n in range(N):
    temp = list(stdin.readline().rstrip())
    for m in range(M):
        if temp[m] == "I":
            startX,startY = n,m
            visit[startX][startY] = True
    campus.append(temp)
person = 0
que = deque([(startX,startY)])
direction = [(-1,0),(1,0),(0,1),(0,-1)]
while que:
    px,py = que.popleft()
    for dx,dy in direction:
        tx,ty = px+dx,py+dy
        if -1< tx < N and -1< ty < M and not visit[tx][ty] and campus[tx][ty] != "X":
            if campus[tx][ty] == "P":
                person+=1
            que.append((tx,ty))
            visit[tx][ty] = True

print( "TT" if not person else person)