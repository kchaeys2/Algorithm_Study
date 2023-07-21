n = int(input())
num = 666
while True:
    if str(num).find('666') >= 0:
        n-=1
        if n < 1:
            break
    num+=1
print(num)
