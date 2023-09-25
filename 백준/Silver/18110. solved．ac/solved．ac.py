from sys import stdin

N = int(stdin.readline().rstrip())
def customRound(num):
    return int(num) if num - int(num) < 0.5 else int(num)+1
if N > 0:
    
    n = [0 for _ in range(N)]

    m = customRound(N*0.15)

    for i in range(N):
        n[i] = int(stdin.readline().rstrip())
    n.sort()
    if m > 0:
        print(customRound(sum(n[m:-m])/len(n[m:-m])))
    else:
        print(customRound(sum(n)/len(n)))
else:
    print(0)
