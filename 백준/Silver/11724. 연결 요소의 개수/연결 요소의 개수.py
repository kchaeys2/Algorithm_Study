from sys import stdin
import sys
sys.setrecursionlimit(10000)
N,M = map(int,stdin.readline().split())
node = [[] for _ in range(N+1)]
count = 0
visit = [False] * (N+1)

def dfs(node,n,visit):
    visit[n] = True
    for i in node[n]:
        if not visit[i]:
            dfs(node,i,visit)

for m in range(M):
    u,v = map(int,stdin.readline().split())
    node[u].append(v)
    node[v].append(u)

for n in range(1,N+1):
    if not visit[n]:
        dfs(node,n,visit)
        count+=1
print(count)