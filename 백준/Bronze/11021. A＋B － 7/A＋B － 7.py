count = int(input())
list = []
for i in range(count):
    a,b = map(int,input().split())
    list.append(a+b)
num = 0
for plus in list:
    num+=1
    print("Case #%d:"%num,plus)