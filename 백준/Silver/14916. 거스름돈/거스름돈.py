from sys import stdin

N = int(stdin.readline().rstrip())
res=-1
for i in range(N//2,-1,-1):
    five = (N-2*i)//5
    if (2*i) + five*5 == N:
        res = i+five
print(res)