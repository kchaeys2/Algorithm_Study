listA = []
listB = []
N,M = map(int,input().split())
for i in range(N):
    listA.append(list(map(int,input().split())))
for i in range(N):
    listB.append(list(map(int,input().split())))


for i in range(N):
    for j in range(M):
        listB[i][j]+=listA[i][j]
    print(*listB[i])