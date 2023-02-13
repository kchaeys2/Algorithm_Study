num = int(input())
result = ""
for i in range(num):
    a = input()
    result += a[0]+a[len(a)-1]+"\n"
print(result[:-1])
