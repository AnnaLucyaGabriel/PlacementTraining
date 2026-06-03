v=list(map(int,input().split()))
k=v[0]
for i in range(0,len(v)):
    if i==len(v)-1:
        v[i]=k
    else:
        v[i]=v[i+1]
print(v)
    