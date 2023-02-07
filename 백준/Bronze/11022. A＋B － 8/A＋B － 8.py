count = int(input())
list = []
for i in range(count):
    a,b=map(int,input().split())
    list.append([a,b,a+b])
num = 0
for p1,p2,p3 in list:
    num+=1
    print("Case #%d: %d + %d = %d" %(num,p1,p2,p3))