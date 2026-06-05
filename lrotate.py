#not optimized
v=list(map(int,input().split()))
k=int(input())
n=len(v)
# for j in range(r):
#     k=v[0]
#     for i in range(0,len(v)):
#         if i==len(v)-1:
#             v[i]=k
#         else:
#             v[i]=v[i+1]
k=k%n
def rotate(i,j):
    while i<j:
        v[i],v[j]=v[j],v[i]
        i+=1
        j-=1

rotate(0,k-1)
rotate(k,n-1)
rotate(0,n-1)
print(v)