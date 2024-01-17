from sys import stdin

N = int(stdin.readline().rstrip())

print("CY") if N%2 == 0 else print("SK")