from sys import stdin

N = int(stdin.readline().rstrip())
for _ in range(N):
    floor = int(stdin.readline().rstrip())
    unit = int(stdin.readline().rstrip())
    btn = [[i for i in range(1,unit+1)]]
    
    for f in range(1,floor+1):
        floors = []
        temp = 0
        for u in range(0,unit):
            temp+=btn[f-1][u]
            floors.append(temp)
        btn.append(floors)
    print(btn[-1][-1])