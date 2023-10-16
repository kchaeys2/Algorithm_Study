from sys import stdin

N = int(stdin.readline().rstrip())

fList = [1,1,2]
def f(num):
   length = len(fList)
   if length-1 < num:
      for i in range(length,num+1):
         fList.append(fList[i-1]*i)
   return fList[num]

result = 0
one = 0
for n in range(N,-1,-2):
   result+=f(one+n)//f(one)//f(n)
   one+=1
print(result%10007)