from sys import stdin
from collections import deque

N,M,K,X = map(int,stdin.readline().split())
direct = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,stdin.readline().split())
    direct[a].append(b)
distance = [0]*(N+1)
que = deque([X])
distance[X] = 1
while que:
    node = que.popleft()
    for n in direct[node]:
        if not distance[n]:
            que.append(n)
            distance[n] = distance[node]+1
flag = False
for d in range(N+1):
    if distance[d] == K+1:
        flag = True
        print(d)
if not flag:
    print(-1)
        