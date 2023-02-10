list = [False for i in range(31)]
for i in range(28):
    list[int(input())] = True
index = 1
for i in list[1:]:
    if(i == False):
        print(index)
    index+=1