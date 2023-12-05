from sys import stdin
from collections import deque

M,N,H = map(int,stdin.readline().split())

tomato = []
que = deque()

for h in range(H):
    temp = []
    for n in range(N):
        t = list(map(int,stdin.readline().split()))
        for m in range(M):
            if t[m] == 1:
                que.append((h,n,m))
        temp.append(t)
    tomato.append(temp)

while que:
    ph,pn,pm = que.popleft()
    for dh,dn,dm in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,1),(0,0,-1)]:
        th,tn,tm = ph+dh,pn+dn,pm+dm
        if -1<th<H and -1<tn<N and -1<tm<M and tomato[th][tn][tm] == 0:
            tomato[th][tn][tm] = tomato[ph][pn][pm] + 1
            que.append((th,tn,tm))

result = 0
for h in tomato:
    for n in h:
        if 0 in n:
            print(-1)
            exit(0)
        result = max(result,max(n))
print(result-1)