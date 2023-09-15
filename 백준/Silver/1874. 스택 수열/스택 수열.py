from sys import stdin

N = int(stdin.readline().rstrip())
stack = []
a = []

last = 0
for _ in range(N):
    c = int(stdin.readline().rstrip())

    for i in range(last+1,N+1):
        if len(stack)> 0 and stack[len(stack)-1] == c:
            stack.pop()
            a.append("-")
            break
        elif i == c:
            a.append("+")
            a.append("-")
            last = i
            break
        else:
            stack.append(i)
            a.append("+")
    if last == N:
        if len(stack)> 0 and stack[len(stack)-1] == c:
            stack.pop()
            a.append("-")
    
if len(stack) > 0:
    print("NO")
else:
    for i in a:
        print(i)