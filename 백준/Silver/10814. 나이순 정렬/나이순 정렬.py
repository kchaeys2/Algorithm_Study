import sys

n = int(sys.stdin.readline())
li = []
for i in range(n):
    age, name = input().split()
    li.append([int(age),name])
li.sort(key=lambda a:a[0])
for i in li:
    print(i[0],i[1])