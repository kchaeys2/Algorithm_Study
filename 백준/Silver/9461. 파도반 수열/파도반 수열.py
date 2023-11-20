from sys import stdin
T = int(stdin.readline().rstrip())

line = [0,1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for _ in range(T):
    N = int(stdin.readline().rstrip())
    if len(line)-1 < N:
        for i in range(len(line),N+1):
            line.append(line[i-2]+line[i-3])
    print(line[N])