list = []
while(True):
    try:
        a,b = map(int,input().split())
        list.append(a+b)
    except EOFError:
        break
for i in list:
    print(i)