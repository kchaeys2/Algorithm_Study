from sys import stdin

N = int(stdin.readline().rstrip())
stack = []
for _ in range(N):
    c = stdin.readline().rstrip()
    if "push" in c:
        stack.append(c[5:])
    elif "pop" in c:
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif "size" in c:
        print(len(stack))
    elif "empty" in c:
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif "top" in c:
        if len(stack) > 0:
            print(stack[len(stack)-1])
        else:
            print(-1)
