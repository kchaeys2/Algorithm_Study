from sys import stdin

input = stdin.readline

N = int(input().rstrip())

a,b = map(int,input().split())
M = int(input().rstrip())

relation = [[] for _ in range(N+1)]
visited = [-1]*(N+1)
flag = False
for _ in range(M):
    x,y = map(int,input().split())
    relation[x].append(y)
    relation[y].append(x)

def dfs(n):
    if n == b:
        return visited[n]
    for rel in relation[n]:
        if visited[rel] < 0:
            visited[rel] = visited[n]+1
            dfs(rel)
visited[a] +=1
dfs(a)
print(visited[b])
