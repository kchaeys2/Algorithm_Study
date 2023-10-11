from sys import stdin

N = int(stdin.readline().rstrip())
n = []
for _ in range(N):
    n.append(int(stdin.readline().rstrip()))

if N > 2:
    m = [0]*N
    m[0] = n[0]
    m[1] = n[0]+n[1]
    m[2] = max(n[0]+n[2],n[1]+n[2])

    for i in range(3,N):
        m[i] = max(m[i-3]+n[i-1]+n[i],m[i-2]+n[i])
    print(m[N-1])
else:
    print(sum(n))
