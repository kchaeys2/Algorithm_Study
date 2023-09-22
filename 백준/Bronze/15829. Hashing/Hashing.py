from sys import stdin

_ = int(stdin.readline().rstrip())
A = stdin.readline().rstrip()

i,sum=0,0
for a in A:
    sum += (ord(a)-96)*(31**i)
    i+=1
print(sum%1234567891)
