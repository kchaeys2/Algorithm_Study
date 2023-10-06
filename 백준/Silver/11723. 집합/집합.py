from sys import stdin

M = int(stdin.readline().rstrip())
S = set()
for _  in range(M):
    order = stdin.readline().rstrip()
    if "add" in order:
        S.add(int(order[4::]))
    elif "remove" in order:
        S.discard(int(order[7::]))
    elif "check" in order:
        if int(order[6::]) in S:
            print(1)
        else:
            print(0)
    elif "toggle" in order:
        x = int(order[7::])
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif "all" in order:
        S.clear()
        S.update([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    else:
        S.clear()