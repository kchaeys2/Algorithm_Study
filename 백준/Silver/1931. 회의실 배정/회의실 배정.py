from sys import stdin

N = int(stdin.readline().rstrip())

l = []
for _ in range(N):
    s,e = map(int,stdin.readline().split())
    l.append((s,e))

l.sort(key = lambda L:(L[1],L[0]))
count = 1
time = l[0][1]
for i in l[1:]:
    if i[0] >= time:
        count+=1
        time = i[1]
print(count)