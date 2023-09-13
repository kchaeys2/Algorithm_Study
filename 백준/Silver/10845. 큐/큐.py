from sys import stdin
from collections import deque
N = int(stdin.readline().rstrip())
stack = deque()
for _ in range(N):
    c = stdin.readline().rstrip()
    if "push" in c:
        stack.append(c[5:])
    elif "pop" in c:
        if len(stack) > 0:
            print(stack.popleft())
        else:
            print(-1)
    elif "size" in c:
        print(len(stack))
    elif "empty" in c:
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif "front" in c:
        if len(stack) > 0:
            print(stack[0])
        else:
            print(-1)
    elif "back" in c:
        if len(stack) > 0:
            print(stack[len(stack)-1])
        else:
            print(-1)