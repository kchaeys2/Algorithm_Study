from sys import stdin
from collections import deque

T = int(stdin.readline().rstrip())

for _ in range(T):
    l = int(stdin.readline().rstrip())
    chase = [[0]*l for _ in range(l)]
    visit = [[False]*l for _ in range(l)]

    x,y = map(int,stdin.readline().split())
    rx,ry = map(int,stdin.readline().split())

    que = deque([(x,y)])
    while que:
        x,y = que.popleft()
        visit[x][y] = True
        if x == rx and y == ry:
            break
        for dx,dy in [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]:
            tx,ty = x+dx,y+dy
            if -1<tx<l and -1<ty<l and not visit[tx][ty]:
                visit[tx][ty] = True
                chase[tx][ty] = chase[x][y]+1
                que.append((tx,ty))
    print(chase[rx][ry])
