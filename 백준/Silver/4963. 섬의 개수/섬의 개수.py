from sys import stdin
from collections import deque

while 1:
    W,H = map(int,stdin.readline().split())
    
    if H < 1:
        break

    land = []
    visit = [[False]*W for _ in range(H)]
    result = 0
    for h in range(H):
        land.append(list(map(int,stdin.readline().split())))

    for h in range(H):
        for w in range(W):
            if not visit[h][w] and land[h][w]:
                visit[h][w] = True
                que = deque([(h,w)])

                while que:

                    x,y = que.popleft()
                    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                        tx,ty = x+dx, y+dy
                        if -1<tx<H and -1<ty<W and not visit[tx][ty] and land[tx][ty]:
                            visit[tx][ty] = True
                            que.append((tx,ty))

                result+=1
    print(result)
