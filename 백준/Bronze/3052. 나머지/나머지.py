stack = []
for i in range(10):
    num = int(input())
    if num%42 in stack:
        pass
    else:
        stack.append(num%42)
print(len(stack))