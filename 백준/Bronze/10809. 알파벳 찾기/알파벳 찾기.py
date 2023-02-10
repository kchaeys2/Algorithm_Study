from string import ascii_lowercase

a = input()
alpha = list(ascii_lowercase)
for b in alpha:
    try:
        print(a.index(b),end = " ")
    except(ValueError):
        print(-1,end=" ")