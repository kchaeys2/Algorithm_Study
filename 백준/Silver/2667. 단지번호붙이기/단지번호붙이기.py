from sys import stdin

N = int(stdin.readline().rstrip())

graph = [list(map(int,stdin.readline().rstrip())) for _ in range(N)]
visit = [[False]*N for _ in range(N)]

groups = []
group = 0
def dfs(graph,x,y,visit):
    global group
    visit[x][y] = True
    for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
        tx,ty = x+dx,y+dy
        if -1<tx<N and -1<ty<N and not visit[tx][ty] and graph[tx][ty] == 1:
            dfs(graph,tx,ty,visit)
            group+=1

for i in range(N):
    for j in range(N):
        if not visit[i][j] and graph[i][j] == 1:
            group=1
            dfs(graph,i,j,visit)
            groups.append(group)
print(len(groups))
for g in sorted(groups):
    print(g)