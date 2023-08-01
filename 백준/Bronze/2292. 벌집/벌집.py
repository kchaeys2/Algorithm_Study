n = int(input())
i,result=1,0
if n == 1:
    result+=1

while n-i>0:
    i+=6*result
    result+=1

print(result)