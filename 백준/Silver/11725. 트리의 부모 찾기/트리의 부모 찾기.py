from sys import stdin
import sys
sys.setrecursionlimit(10**8)
N = int(stdin.readline().rstrip())

node = [[] for _ in range(N+1)]
visit = [0]*(N+1)

for i in range(1,N):
    a,b = map(int,stdin.readline().split())
    node[a].append(b)
    node[b].append(a)


def dfs(start):
    for i in node[start]:
        if not visit[i]:
            visit[i] = start
            dfs(i)
dfs(1)
for i in range(2,N+1):
    print(visit[i])