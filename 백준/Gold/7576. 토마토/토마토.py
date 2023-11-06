from sys import stdin
from collections import deque

input = stdin.readline
M,N = map(int,input().split())
boxes = []
visit = [[False]*M for _ in range(N)]
que = deque([])
for n in range(N):
    box = list(map(int,input().split()))
    for m in range(M):
        if box[m] == 1:
            que.append((n,m))
            visit[n][m] = True

    boxes.append(box)
direction = [(-1,0),(1,0),(0,1),(0,-1)]

while que:
    px,py = que.popleft()
    for dx,dy in direction:
        tx,ty = px+dx,py+dy
        
        if -1 < tx < N and -1 < ty < M and not visit[tx][ty] and boxes[tx][ty] != -1:
            visit[tx][ty] = True
            boxes[tx][ty] = boxes[px][py] + 1
            que.append((tx,ty))
res = 0
for box in boxes:
    if 0 in box:
        print(-1)
        exit(0)
    res = max(res,max(box))

print(res-1)