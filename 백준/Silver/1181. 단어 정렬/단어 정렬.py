n = int(input())
li=set({})
for i in range(n):
    li.add(input())
li = list(li)
temp=""

for i in range(len(li)):
    for j in range(i):
        if len(li[i]) <= len(li[j]):
            temp = li[i]
            li[i]=li[j]
            li[j]=temp
        if len(li[i]) == len(li[j]):
            for k in range(len(li[i])):
                if ord(li[i][k]) < ord(li[j][k]):
                    temp = li[i]
                    li[i]=li[j]
                    li[j]=temp
                    break
                elif ord(li[i][k]) > ord(li[j][k]):
                    break
for l in li:
    print(l)