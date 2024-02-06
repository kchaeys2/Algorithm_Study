from sys import stdin
import sys 
sys.setrecursionlimit(10**6)

input = stdin.readline

M,N = map(int,input().split())

Figure = []
for _ in range(M):
    n = list(map(int,input().rstrip()))
    Figure.append(n)

def dfs(start,visited):
    x,y = start
    visited[x][y] = True
    for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
        tx,ty = x+dx,y+dy
        if -1<tx<M and -1<ty<N and not visited[tx][ty] and Figure[tx][ty] == 0:
              
            dfs((tx,ty),visited)
percolate = False
for n in range(N):
    if Figure[0][n] == 0:
        visited = [[False]*N for _ in range(M)]
        dfs((0,n),visited)
        if True in visited[M-1]:
            percolate = True
            print("YES")
            break

if not percolate:
    print("NO")