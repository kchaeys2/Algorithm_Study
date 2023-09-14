from sys import stdin

while True:
    c = stdin.readline().rstrip()
    stack = []
    if c == ".":
        break
    for i in c:
        if i in ('(',')','[',']'):
            if len(stack) > 0:
                if stack[len(stack)-1] + i == "()":
                    stack.pop()
                elif stack[len(stack)-1] + i == "[]":
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)

    if len(stack) > 0:
        print("no")
    else:
        print("yes")
    