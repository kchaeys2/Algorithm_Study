from sys import stdin
from collections import deque

N,M = map(int,stdin.readline().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    A,B = map(int,stdin.readline().split())
    graph[B].append(A)

res = []
for i in range(1,N+1):
    visited = [False]*(N+1)
    count = 1
    que = deque([i])
    visited[i] = True
    while que:
        node = que.popleft()
        for n in graph[node]:
            if not visited[n]:
                visited[n] = True
                que.append(n)
                count+=1
    res.append(count)
mx= max(res)
for n in range(N):
    if res[n] == mx:
        print(n+1,end=" ")
