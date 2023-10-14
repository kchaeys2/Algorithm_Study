from sys import stdin

N,M = map(int,stdin.readline().split())
n = list(map(int,stdin.readline().split()))

sumList = [n[0],n[0]+n[1]]

for _ in range(M):
   I,J = map(int,stdin.readline().split())
   length = len(sumList)
   if length < J:
      for j in range(length,J):
         sumList.append(sumList[j-1]+n[j])

   if I-2 < 0:
       print(sumList[J-1])
   else:
      print(sumList[J-1]-sumList[I-2])