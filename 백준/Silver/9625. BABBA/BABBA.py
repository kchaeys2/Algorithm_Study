from sys import stdin

N = int(stdin.readline().rstrip())

btn = [0]*46
btn[0] = (1,0)
btn[1] = (0,1)
for i in range(2,N+1):
    btn[i] = (btn[i-2][0]+btn[i-1][0],btn[i-2][1]+btn[i-1][1])
print(btn[N][0],btn[N][1])