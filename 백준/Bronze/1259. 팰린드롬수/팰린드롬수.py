n=""
while n != "0":
    n = input()
    if n == "0":
        break
    print("yes") if n == n[::-1] else print("no")