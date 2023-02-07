sum=0
for i in range(0,5):
    a=int(input())
    a= 40 if a<40 else a
    sum+=a;
sum//=5
print(sum)