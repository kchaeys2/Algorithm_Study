from sys import stdin
from collections import deque
N = int(stdin.readline().rstrip())
graph = [[] for _ in range(N)]
res = []
for i in range(N):
    temp = list(map(int,stdin.readline().split()))
    for j in range(N):
        if temp[j] == 1:
            graph[i].append(j)

for n in range(N):
    temp = [0]*N
    que = deque(graph[n])
    while que:
        node = que.popleft()
        if not temp[node]:
            temp[node] = 1
            for v in graph[node]:
                que.append(v)
    res.append(temp)
for i in res:
    for j in i:
        print(j,end=" ")
    print("")