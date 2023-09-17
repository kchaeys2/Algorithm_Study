from sys import stdin

N = int(stdin.readline().rstrip())
li = [0 for _ in range(N)]
for i in range(N):
    li[i] = list(map(int,stdin.readline().split()))
result = sorted(li,key = lambda x : (x[1], x[0]))

for i in result:
    print(i[0],end=" ")
    print(i[1])