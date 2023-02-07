T = int(input())
sum =[]
for i in range(0,T):
    a,b = map(int,input().split())
    sum.append(a+b)
for i in sum:
    print(i)