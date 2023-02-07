day=int(input())
car = list(map(int,input().split()))
answer=0
for i in range(0,5):
    answer = answer+1 if car[i]==day else answer
print(answer)