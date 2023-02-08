listCount,num = map(int,input().split())
list = list(map(int,input().split()))
result = []
for s in list:
    if(s<num):
        result.append(s)
print(*result)