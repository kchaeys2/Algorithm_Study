n = int(input())
def fac(n):
    if n == 0:
        return 1
    return fac(n-1)*n
sn = str(fac(n))
n=0
for i in sn[::-1]:
    if i != "0":
        break
    n+=1
print(n)
