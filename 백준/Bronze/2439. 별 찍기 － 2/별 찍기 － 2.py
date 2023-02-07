count = int(input())
for i in range(1,count+1):
    if(i == count+1):
        print("*"*i)
    else:
        print(" "*(count-i)+("*"*i))