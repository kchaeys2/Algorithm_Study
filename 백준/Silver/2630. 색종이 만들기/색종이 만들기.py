from sys import stdin

N = int(stdin.readline().rstrip())

L = []
for _ in range(N):
    L.append(list(map(int,stdin.readline().split())))

blue,white = 0,0
def dfs(start,length):
    global blue,white
    startPoint = L[start[0]][start[1]]

    for x in range(start[0],start[0]+length):
        for y in range(start[1],start[1]+length):
            if L[x][y] != startPoint:
                dfs(start,length//2)
                dfs((start[0],start[1]+length//2),length//2)
                dfs((start[0]+length//2,start[1]),length//2)
                dfs((start[0]+length//2,start[1]+length//2),length//2)
                return
    if startPoint == 1:
        blue+=1
    else:
        white+=1

dfs((0,0),N)
print(white)
print(blue)
