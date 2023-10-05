from sys import stdin

N = int(stdin.readline().rstrip())
P = list(map(int,stdin.readline().split()))

P.sort()
sum = 0
result = 0
for p in P:
    sum+=p
    result+=sum
print(result)