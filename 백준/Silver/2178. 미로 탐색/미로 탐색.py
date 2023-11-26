from sys import stdin
from collections import deque

N,M = map(int,stdin.readline().split())
miro = [list(map(int,stdin.readline().rstrip())) for _ in range(N)]

end = [[0]*M for _ in range(N)]
que = deque([(0,0)])
end[0][0]+=1

while que:
    x,y = que.popleft()
    for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
        tx,ty = x+dx,y+dy
        if -1< tx <N and -1<ty<M and not end[tx][ty] and miro[tx][ty] == 1:
            end[tx][ty] = end[x][y]+1
            que.append((tx,ty))
print(end[N-1][M-1])