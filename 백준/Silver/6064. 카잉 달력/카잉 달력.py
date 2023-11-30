from sys import stdin

T = int(stdin.readline().rstrip())

for _ in range(T):
    M,N,x,y = map(int,stdin.readline().split())

    while  x <= M*N:
        if not (x-y)%N :
            print(x)
            break
        x+=M
    else:
        print(-1)