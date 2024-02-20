from sys import stdin

X,Y = map(int,stdin.readline().split())
Z = (Y*100)//X

def binary(start,end):
    res = 0
    while start <= end:
        mid = (start+end)//2
        if (Y+mid)*100 // (X+mid) > Z:
            res = mid
            end = mid-1
        else:
            start = mid + 1
    return res
if Z > 98:
    print(-1)
else:
    print(binary(0,1000000000))