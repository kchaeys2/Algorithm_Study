count = int(input())
list = list(map(int,input().split()))
same = int(input())
count = 0
for i in list:
    if(i == same):
        count+=1
print(count)