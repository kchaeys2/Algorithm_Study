from sys import stdin

K,N = map(int,stdin.readline().split())
k=[]
for _ in range(K):
    k.append(int(stdin.readline().rstrip()))

def binary(li,start,end,target):
    while start <= end:
        mid  = (start+end)//2
        temp = 0
        for i in li:
            if i >= mid:
                temp+=i//mid

        if temp == target:
            start = mid+1
        elif temp < target:
            end = mid-1
        else:
            start = mid+1
        
    return end


print(binary(k,1,max(k),N))
