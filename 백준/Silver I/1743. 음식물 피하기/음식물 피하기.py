from sys import stdin
import sys
sys.setrecursionlimit(10**6)

N,M,K = map(int,stdin.readline().split())
N+=1
M+=1
graph = [[False]*(M) for _ in range(N)]
for _ in range(K):
    r,c = map(int,stdin.readline().split())
    graph[r][c] = True

visited = [[False]*(M) for _ in range(N)]
def dfs(start):
    global res
    x,y = start
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        tx,ty = x+dx,y+dy
        if 0<tx<M and 0<ty<N and not visited[ty][tx] and graph[ty][tx]:
            visited[ty][tx] = True
            res+=1
            dfs((tx,ty))
mx = 0
for n in range(1,N):
    for m in range(1,M):
        if graph[n][m]:
            res = 1
            visited[n][m] = True
            dfs((m,n))
            mx = max(mx,res)
print(mx)