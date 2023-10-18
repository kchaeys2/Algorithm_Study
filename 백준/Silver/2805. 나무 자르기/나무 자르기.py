from sys import stdin

_ ,M = map(int,stdin.readline().split())
tree = list(map(int,stdin.readline().split()))

left,right = 1,max(tree)
while left <= right:
    result = 0
    mid = (left+right)//2
    for t in tree:
        if t > mid:
            result+=t-mid
        if result >= M:
            break
    if result >= M:
        left = mid+1
    else:
        right = mid-1
print(right)
