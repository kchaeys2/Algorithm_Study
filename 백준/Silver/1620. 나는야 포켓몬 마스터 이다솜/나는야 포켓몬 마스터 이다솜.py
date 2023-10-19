from sys import stdin

N ,M = map(int,stdin.readline().split())

dicN={}
dicS = {}
for i in range(1,N+1):
    dicN[i] = stdin.readline().rstrip()
    dicS[dicN[i]] = i
for _ in range(M):
    m = stdin.readline().rstrip()
    try:
        print(dicN[int(m)])
    except:
        print(dicS[m])