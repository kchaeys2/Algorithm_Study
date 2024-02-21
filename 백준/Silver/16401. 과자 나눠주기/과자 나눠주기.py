import sys
input = sys.stdin.readline

m, n  = map(int,input().split())
L = list(map(int, input().split()))

def binary(start,end):
    answer = 0
    while start <= end:
        mid = (start+end)//2
        c = 0 
        for i in L:
            c += i//mid
        if c >=m:
            answer = max(answer,mid)
            start = mid + 1
        else:
            end = mid - 1
    return answer
print(binary(1,1000000000))