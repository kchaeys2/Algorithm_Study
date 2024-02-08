from sys import stdin
import sys
sys.setrecursionlimit(10**6)

input = stdin.readline
M,N,K = map(int,input().split())

monon = [[0]*N for _ in range(M)]
visited = [[False]*N for _ in range(M)]
for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    for dx in range(x1,x2):
        for dy in range(y2-1,y1-1,-1):
            monon[dy][dx] = 1
def dfs(start):
    global count
    count+=1
    x,y = start
    visited[x][y] = True
    for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
        tx,ty = x+dx,y+dy
        if -1<tx<M and -1<ty<N and not visited[tx][ty] and monon[tx][ty] == 0:
            dfs((tx,ty))

counts = []
for y in range(N):
    for x in range(M):
        if not visited[x][y] and monon[x][y] == 0:
            count = 0
            dfs((x,y))
            counts.append(count)
print(len(counts))
for count in sorted(counts) :
    print(count, end= " ")