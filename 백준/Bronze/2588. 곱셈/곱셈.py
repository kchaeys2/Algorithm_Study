A = int(input())
B = int(input())
C = B
b= []
while(B!=0):
    b.append(B%10)
    B//=10
print(A*b[0])
print(A*b[1])
print(A*b[2])
print(A*C)