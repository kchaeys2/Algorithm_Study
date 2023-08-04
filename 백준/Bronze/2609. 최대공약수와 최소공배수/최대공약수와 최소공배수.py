a,b= map(int,input().split())

def uc(a,b):
    if a<b:
        a,b = b,a
    if a%b==0:
        return b
    else:
        return uc(b,a%b)
res = uc(a,b)
print(res)
print(a*b//res)