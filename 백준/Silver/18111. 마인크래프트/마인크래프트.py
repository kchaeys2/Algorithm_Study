from sys import stdin

N,C,B = map(int,stdin.readline().split())
M = [0 for _ in range(N*C)]
i=0
for _ in range(N):
    temp = list(map(int,stdin.readline().split()))
    for t in temp:
        M[i] = t
        i+=1
secList = {}
for i in range(0,max(M)+1):
    b=B
    sec = 0
    for m in M:
        temp = m-i
        if temp > 0:
            b += temp
            sec+=temp*2
        else:
            b +=temp
            sec+=temp*-1
    if b >= 0:
        secList[sec] = i
resmin = min(secList.keys())
print(resmin,end=" ")
print(secList[resmin])
