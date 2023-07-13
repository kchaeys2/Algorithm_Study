num = int(input())
li = list(map(int,input().split()))
result = len(li)
for i in li:
    if(i == 1):
        result-=1
    
    for j in range(2,int(i**(1/2))+1):
        if(i%j==0):
            result-=1
            break
print(result)