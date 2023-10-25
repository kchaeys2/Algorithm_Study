from sys import stdin
import heapq

N = int(stdin.readline().rstrip())
que = []
for _ in range(N):
    x = int(stdin.readline().rstrip())

    if x > 0:
        heapq.heappush(que,x)
    else:
        try:
            print(heapq.heappop(que))
        except:
            print(0)