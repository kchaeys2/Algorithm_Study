num = int(input())

def divSum(num):
    for i in range(2,num):
        temp = i
        res = temp

        while temp>0:
            res += temp%10
            temp //=10
            
        if res == num:
            return i
    return 0
print(divSum(num))
