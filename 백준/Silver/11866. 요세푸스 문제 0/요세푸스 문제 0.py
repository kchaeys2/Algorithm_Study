import sys

N,K = map(int,sys.stdin.readline().split())
stack = [i for i in range(1,N+1)]
res = []
i=0
while stack:
    i +=K-1
    if i >= len(stack):
        i %=len(stack)
    res.append(str(stack.pop(i)))
print("<"+", ".join(res[:])+">")