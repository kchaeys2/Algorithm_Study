from sys import stdin
import sys

sys.setrecursionlimit(1000000)

N = int(stdin.readline().rstrip())
picture = [list(stdin.readline().rstrip()) for _ in range(N)]

colorThree = [[False]*N for _ in range(N)]

def colorT(picture,x,y,colorThree):
    global target
    colorThree[x][y] = True
    for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
        tx,ty = x+dx,y+dy
        if -1<tx<N and -1<ty<N and not colorThree[tx][ty] and picture[tx][ty] == target:
            add=True
            colorT(picture,tx,ty,colorThree) 

dictThree = {"R":0,"G":0,"B":0}
for i in range(N):
    for j in range(N):
        target = picture[i][j]
        if not colorThree[i][j]:
            colorT(picture,i,j,colorThree)
            dictThree[target]+=1

dictTwo = {"R":0,"B":0}
for i in range(N):
    for j in range(N):
        if picture[i][j] == "G":
            picture[i][j]="R"

colorThree = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        target = picture[i][j]
        if not colorThree[i][j]:
            colorT(picture,i,j,colorThree)

            dictTwo[target]+=1
print(sum(dictThree.values()),sum(dictTwo.values()))