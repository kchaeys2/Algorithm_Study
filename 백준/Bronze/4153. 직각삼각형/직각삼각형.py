result = []
a,b,c = 1,1,1

while a!=0 or b!=0 or c!=0:
    a,b,c = map(int,input().split())
    a,b,c = a**2,b**2,c**2
    if a == b+c:
        result.append("right")
    elif b == a+c:
        result.append("right")
    elif c == a+b:
        result.append("right")
    else:
        result.append("wrong")
result.pop()
for i in result:
    print(i)