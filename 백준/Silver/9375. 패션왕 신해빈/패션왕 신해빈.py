from sys import stdin

T = int(stdin.readline().rstrip())

for _ in range(T):
   N = int(stdin.readline().rstrip())
   n = {}
   for _ in range(N):
      name,category = stdin.readline().split()
      if category in n:
         n[category].append(name)
      else:
         n[category] = [name]
   result = 1
   for i in n:
      result*=(len(n[i])+1)
   print(result-1)
