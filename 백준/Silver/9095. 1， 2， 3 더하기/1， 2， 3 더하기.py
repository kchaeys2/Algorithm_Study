from sys import stdin

T = int(stdin.readline().rstrip())

fact = [1,1,2,6]

def f(num):
   length = len(fact)-1
   if length < num:
      for i in range(length,num):
         fact.append(fact[i]*(i+1))
   return fact[num]

for _ in range(T):
   num = int(stdin.readline().rstrip())
   result = 0
   for i in range(0,num+1,2):
      temp = num
      temp-=i
      for j in range(0,temp+1,3):
         one,two,three = num-i-j,i//2,j//3
         result+=f(one+two+three)//f(one)//f(two)//f(three)
   print(result)
