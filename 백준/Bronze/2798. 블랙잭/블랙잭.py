n,max = map(int,input().split())
card = list(map(int,input().split()))
max_n = 0 
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            temp = card[i]+card[j]+card[k]
            if temp > max:
                continue
            elif temp > max_n:
                max_n = temp
print(max_n)