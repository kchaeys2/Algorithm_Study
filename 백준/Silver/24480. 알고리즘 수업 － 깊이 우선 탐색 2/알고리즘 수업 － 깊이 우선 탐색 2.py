from sys import stdin
import sys
sys.setrecursionlimit(10**6)
N,M,R = map(int,stdin.readline().split())

nodes = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,stdin.readline().split())
    nodes[u].append(v)
    nodes[v].append(u)
visited = [0]*(N+1)
def dfs(n):
    global count
    for node in sorted(nodes[n],reverse=True):
        if not visited[node]:
            count+=1
            visited[node] = count
            dfs(node)
count = 1
visited[R] = count
dfs(R)
for i in range(1,N+1):
    print(visited[i])