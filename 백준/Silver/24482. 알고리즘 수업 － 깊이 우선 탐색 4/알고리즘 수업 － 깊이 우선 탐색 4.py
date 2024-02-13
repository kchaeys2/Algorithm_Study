from sys import stdin
import sys
sys.setrecursionlimit(10**6)
N,M,R = map(int,stdin.readline().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [-1]*(N+1)
def dfs(start):
    for n in sorted(graph[start],reverse=True):
        if visited[n] < 0:
            visited[n] = visited[start] + 1
            dfs(n)
visited[R] = 0
dfs(R)
for i in range(1,N+1):
    print(visited[i])