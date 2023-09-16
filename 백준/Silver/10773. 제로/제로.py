N = int(input())

stack = []
for _ in range(N):
    c = int(input())
    if c > 0 :
        stack.append(c)
    else:
        stack.pop()
print(sum(stack))