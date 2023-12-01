from sys import stdin
import heapq
N = int(stdin.readline().rstrip())

heap = []
for _ in range(N):
    x = int(stdin.readline().rstrip())
    if not x:
        try:
            print(heapq.heappop(heap)[1])
        except:
           print(0)
    else:
        heapq.heappush(heap,(abs(x),x))
    
