N = int(input())


for _ in range(N):
    stack = []
    c = input()
    if len(c) % 2 != 0:
        print("NO")
    else:
        stack.append(c[0])
        for i in range(1, len(c)):
            stack.append(c[i])
            lengthS = len(stack)
            if lengthS > 1: 
                if stack[lengthS-2]+stack[lengthS-1] == "()":
                    stack.pop()
                    stack.pop()

        if len(stack) > 0:
            print("NO")
        else:
            print("YES")
