a = int(input())
b = int(input())
c = int(input())

result = str(a*b*c)

alpha = [0 for _ in range(10)]

for i in result:
    num=int(i)
    for j in range(10):
        if(num == j):
            alpha[j]+=1

for i in alpha:
    print(i)