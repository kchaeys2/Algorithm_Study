n = int(input())
st = []

for i in range(n):
    li = list(map(int,input().split()))
    li.append(1)
    st.append(li)

for i in range(n):
    for j in range(i,n):
        if st[i][0] < st[j][0] and st[i][1] < st[j][1]:
            st[i][2]+=1

        elif st[i][0] > st[j][0] and st[i][1] > st[j][1]:
            st[j][2]+=1
        
for i in range(n):
    print(st[i][2],end=" ")
