from sys import stdin
import sys
sys.setrecursionlimit(10**6)
N,M,R = map(int,stdin.readline().split())
N+=1
graph = [[] for _ in range(N)]
for _ in range(M):
    u,v = map(int,stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [-1]*(N)
def dfs(start,count):
    visited[start] = count
    for node in sorted(graph[start]):
        if visited[node] < 0:
            dfs(node,count+1)
dfs(R,0)
for v in range(1,N):
    print(visited[v])