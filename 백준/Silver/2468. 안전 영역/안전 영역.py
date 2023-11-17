from sys import stdin
import sys,copy
sys.setrecursionlimit(10**6)

N = int(stdin.readline().rstrip())

graph = []
S = set()
for _ in range(N):
    temp = list(map(int,stdin.readline().split()))
    graph.append(temp)
    S.update(temp)
if len(S) == 1:
    print(1)
    exit(0)
def dfs(graph,x,y,visit):
    visit[x][y] = True

    for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
        tx,ty= x+dx,y+dy
        if -1< tx < N and -1< ty <N and not visit[tx][ty]:
            dfs(graph,tx,ty,visit)

water = [[False]*N for _ in range(N)]
safe = 0
for s in sorted(list(S)):
    for i in range(N):
        for j in range(N):
            if not water[i][j] and graph[i][j] <= s:
                water[i][j] = True
    visit = copy.deepcopy(water)
    count = 0
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                dfs(graph,i,j,visit)
                count+=1

    safe = max(safe,count)
print(safe)