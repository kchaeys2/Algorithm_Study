a,b= map(int,input().split())

def fac(n):
    if n==0:
        return 1
    return fac(n-1)*n
print(fac(a)//(fac(a-b)*fac(b)))