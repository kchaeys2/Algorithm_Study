round = int(input())
result = []
for i in range(round):
    ox = input()
    b,score = 0 , 0
    for a in ox:
        if(a == 'O'):
            b+=1
            score +=b
        else:
            b = 0
    result.append(score)

for an in result:
    print(an)