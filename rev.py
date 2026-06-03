v=list(map(int,input().split()))
j=len(v)//4+1
# for i in range(len(v)//2):
#     temp=v[i]
#     v[i]=v[j]
#     v[j]=temp
#     j-=1
for i in range(len(v)//4+1):
    temp=v[i]
    v[i]=v[j]
    v[j]=temp
    j-=1
print(v)