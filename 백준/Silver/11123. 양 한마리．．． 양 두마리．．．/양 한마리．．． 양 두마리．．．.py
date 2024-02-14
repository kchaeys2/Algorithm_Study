from sys import stdin
import sys
sys.setrecursionlimit(10**6)
T = int(stdin.readline().rstrip())

def dfs(start,visited,graph):
        x,y = start

        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            tx, ty = x+dx, y+dy
            if -1<tx<H and -1<ty<W and not visited[tx][ty] and graph[tx][ty] == '#':
                visited[tx][ty] = True
                dfs((tx,ty),visited,graph)

for _ in range(T):
    H,W = map(int,stdin.readline().split())

    graph = []
    for _ in range(H):
        temp = list(stdin.readline().rstrip())
        graph.append(temp)
    visited = [[False]*W for _ in range(H)]

    sleep = 0
    for h in range(H):
        for w in range(W):
            if not visited[h][w] and graph[h][w] == '#':
                visited[h][w] = True
                dfs((h,w),visited,graph)
                sleep +=1
    print(sleep)

