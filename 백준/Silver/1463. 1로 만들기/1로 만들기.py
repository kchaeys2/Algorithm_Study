from sys import stdin

X = int(stdin.readline().rstrip())
res = [None,0,1]
for i in range(3,X+1):
    res.append(res[i-1]+1)
    if i%3 == 0:
        res[i] = min(res[i],res[i//3]+1)
    if i%2 ==0:
        res[i] = min(res[i],res[i//2]+1)
print(res[X])