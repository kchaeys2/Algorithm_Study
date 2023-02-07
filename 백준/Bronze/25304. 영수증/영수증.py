totalPrice = int(input())
count = int(input())

p = 0
for i in range(count):
    price,c = map(int,input().split())
    
    p+=price*c
print("Yes" if p == totalPrice else "No")