from sys import stdin

N = int(stdin.readline().rstrip())
req = list(map(int,stdin.readline().split()))
M = int(stdin.readline().rstrip())

def binary(start,end):
    while start<= end:
        current = 0
        mid = (start+end)//2
        for i in req:
            if i > mid:
                current += mid
            else:
                current += i
        if current <= M :
            start = mid + 1
        else:
            end = mid - 1
    return end
print(binary(0,max(req)))