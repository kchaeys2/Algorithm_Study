num = list(map(int,input().split()))
result=0

for i in range(0,7):
    if(num[i] == (i+1)):
        result += 1
    elif(num[i] == (8-i)):
        result -= 1
    else:
        result = None
        break

if(result == 7):
    print('ascending')
elif(result == -7):
    print('descending')
else:
    print('mixed')


    
