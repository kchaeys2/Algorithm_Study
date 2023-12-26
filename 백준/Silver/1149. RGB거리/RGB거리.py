from sys import stdin

N = int(stdin.readline().rstrip())
home = [list(map(int,stdin.readline().split())) for _ in range(N)]

for h in range(1,len(home)):
    home[h][0] += min(home[h-1][1],home[h-1][2])
    home[h][1] += min(home[h-1][0],home[h-1][2])
    home[h][2] += min(home[h-1][0],home[h-1][1])
print(min(home[N-1])) 