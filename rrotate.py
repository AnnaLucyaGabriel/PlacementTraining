v=list(map(int,input().split()))
temp=v[-1]
for i in range(len(v)-1,0,-1):
    v[i]=v[i-1]
v[0]=temp
print(v)