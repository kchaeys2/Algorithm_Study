from sys import stdin

T = int(stdin.readline().rstrip())

zero = [1,0,1]
one = [0,1,1]
for _ in range(T):
    num = int(stdin.readline().rstrip())
    length = len(zero)
    if num >=length:
        for i in range(length-2,num-1):
            zero.append(zero[i]+zero[i+1])
            one.append(one[i]+one[i+1])
    print(zero[num],one[num])