from sys import stdin

N = int(stdin.readline().rstrip())
n = list(map(int,stdin.readline().split()))
M = int(stdin.readline().rstrip())
m = list(map(int,stdin.readline().split()))
n.sort()

def binary(list,node,start,end):
    if start> end:
        return 0
    mid = (start+end)//2
    if list[mid] == node:
        return 1
    elif node < list[mid]:
        return binary(list,node,start,mid-1)
    else:
        return binary(list,node,mid+1,end)
for node in m:
    print(binary(n,node,0,N-1))
