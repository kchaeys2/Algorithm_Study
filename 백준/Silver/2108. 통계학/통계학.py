from sys import stdin

N = int(stdin.readline().rstrip())

liM = [0 for _ in range(N)]

dict={}
sum = 0

for i in range(N):
    liM[i] = int(stdin.readline().rstrip())
    sum+=liM[i]
    if liM[i] in dict:
        dict[liM[i]]+=1
    else:
        dict[liM[i]]=1

cnt = [k for k,v in dict.items() if max(dict.values()) == v]

liM.sort()
print(round(sum/N))
print(liM[N//2])

if len(cnt) > 1:
    cnt.sort()
    print(cnt[1])
else:
    print(cnt[0])

print(liM[N-1]-liM[0])