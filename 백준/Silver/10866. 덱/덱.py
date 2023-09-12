from collections import deque

deque = deque()

N = int(input())
res = []

for i in range(N):
    order = input()

    if order.startswith("push_front"):
        back = order.split(" ")
        deque.appendleft(back[1])
    elif order.startswith("push_back"):
        back = order.split(" ")
        deque.append(back[1])
    elif order == "pop_front":
        try:
            res.append(deque.popleft())
        except IndexError:
            res.append(-1)

    elif order == "pop_back":
        try:
            res.append(deque.pop())
        except IndexError:
            res.append(-1)
    elif order == "size":
        res.append(len(deque))
    elif order == "empty":
        if len(deque) < 1:
            res.append(1)
        else:
            res.append(0)

    elif order == "front":
        try:
            res.append(deque[0])
        except IndexError:
            res.append(-1)
    elif order == "back":
        try:
            res.append(deque[len(deque)-1])
        except IndexError:
            res.append(-1)

for i in res:
    print(i)
