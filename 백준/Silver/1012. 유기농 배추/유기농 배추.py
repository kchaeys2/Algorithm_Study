from sys import stdin
import sys

sys.setrecursionlimit(10000)

T = int(stdin.readline().rstrip())

def dfs(dict,key):
    for v in dict[key]:
        v[1] = True
        if v[0] in dict and not dict[v[0]][0][1]:
            dfs(dict,v[0])

for _ in range(T):
    dict = {}
    M,N,K = map(int,stdin.readline().split())
    for _ in range(K):
        X,Y = map(int,stdin.readline().split())
        dict[(X,Y)] = [[(X,Y),False],[(X+1,Y),False],[(X-1,Y),False],[(X,Y+1),False],[(X,Y-1),False]]
    
    count = 0
    for k,v in dict.items():
        if not v[0][1]:
            dfs(dict,k)
            count+=1

    print(count)
