num = int(input())
result = []
for i in range(num):
    H,W,N = map(int,input().split())
    h = N%H 
    w = int(N/H)+1
    if(h==0):
        h=H
        w-=1

    if(w < 10):
        cw = "0"+str(w)
    else:
        cw = str(w)
    result.append(str(h)+cw)
for an in result:
    print(an)