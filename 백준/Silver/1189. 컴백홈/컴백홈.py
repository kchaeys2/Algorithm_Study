from sys import stdin

R,C,K = map(int,stdin.readline().split())
graph = [list(stdin.readline().rstrip()) for _ in range(R)]
res = 0
def dfs(depth,x,y):
    global res
    if depth == K and x == 0 and y == C-1:
        res+=1
    for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
        tx,ty = x+dx,y+dy
        if -1<tx<R and -1<ty<C and graph[tx][ty] == ".":
            graph[tx][ty] = "T"
            dfs(depth+1,tx,ty)
            graph[tx][ty] = "."
graph[R-1][0] = "T"
dfs(1,R-1,0)
print(res)            