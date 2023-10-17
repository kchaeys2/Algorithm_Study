from sys import stdin

N = stdin.readline().rstrip()

number,result,plus = "",0,0
for n in N[::-1]:
    if n in "+":
        plus+=int(number[::-1])
        number = ""
    elif n in "-": 
        result-=int(number[::-1])+plus
        number = ""
        plus = 0
    else:
        number+=n    
print(result+plus+int(number[::-1]))