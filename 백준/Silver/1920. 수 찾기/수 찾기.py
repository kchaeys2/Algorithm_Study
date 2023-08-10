import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
ml = list(map(int,sys.stdin.readline().split()))
a.sort()

def binary(l,N,start,end):
    if start> end:
        return 0
    m = (start+end)//2
    if l==N[m]:
        return 1
    elif l < N[m]:
        return binary(l,N,start,m-1)
    else:
        return binary(l,N,m+1,end)
for l in ml:
    start = 0
    end = len(a)-1
    print(binary(l,a,start,end))