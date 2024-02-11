from sys import stdin

board = [list(stdin.readline().split()) for _ in range(5)]

res = set()
def dfs(n,number):  
    if len(number) == 6:
        res.add(number)
        return
    x,y  = n
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        tx,ty = x+dx,y+dy
        if -1<tx<5 and -1<ty<5:
            dfs((tx,ty),number+board[tx][ty])
for i in range(5):
    for j in range(5):
        dfs((i,j),board[i][j])
print(len(res))