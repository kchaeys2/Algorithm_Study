from sys import stdin

N = int(stdin.readline().rstrip())

res = [0]*91
res[1] = 1
for i in range(2,N+1):
    res[i] = res[i-1]+res[i-2]
print(res[N])