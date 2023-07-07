n = input()
alpha = [0 for _ in range(26)]
for i in n:
    for j in range(26):
        if(ord(i) == (65+j) or ord(i) == (97+j)):
            alpha[j]+=1

max = alpha[0]
result = 65
for i in range(1,26):
    if(alpha[i] > max):
        max = alpha[i]
        result = 65+i
        
    elif(alpha[i] == max):
        result = 63

print(chr(result))