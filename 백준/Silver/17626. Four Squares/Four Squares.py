from sys import stdin

N = int(stdin.readline().rstrip())

res = [0]*(N+1)
k=1
while k**2 <= N:
    res[k**2] = 1
    k+=1

for i in range(1,N+1):
    if res[i] == 1 :
        continue
    j = 1
    while j*j <= i:
        if not res[i]:
            res[i] = res[j*j] + res[i-j*j]
        else:
            res[i] = min(res[i],res[j*j]+res[i-j*j])
        j+=1
        
print(res[N])