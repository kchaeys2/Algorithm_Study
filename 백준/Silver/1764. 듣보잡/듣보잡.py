from sys import stdin

N,M = map(int,stdin.readline().split())
n = set([stdin.readline().rstrip() for _ in range(N)])
m = set([stdin.readline().rstrip() for _ in range(M)])
a = list(n&m)
print(len(a))
a.sort()
for i in a:
    print(i)