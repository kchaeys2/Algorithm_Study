import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int,input().split()))
cal = list(map(int,input().split()))

mini = int(1e9)
maxi = int(-1e9)

def dfs(dept,total,plus,minus,mulitiply,divide):
    global mini,maxi
    if dept == N:
        mini = min(mini,total)
        maxi = max(maxi,total)
        return
    if plus:
        dfs(dept+1,total+A[dept],plus-1,minus,mulitiply,divide)
    if minus:
        dfs(dept+1,total-A[dept],plus,minus-1,mulitiply,divide)
    if mulitiply:
        dfs(dept+1,total*A[dept],plus,minus,mulitiply-1,divide)
    if divide:
        dfs(dept+1,int(total/A[dept]),plus,minus,mulitiply,divide-1)

dfs(1,A[0],cal[0],cal[1],cal[2],cal[3])
print(maxi)
print(mini)
