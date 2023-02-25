test = int(input())
result = ""
for i in range(test):
    num,s = input().split()
    for j in s:
        result+=j*int(num)
    print(result)
    result = ""