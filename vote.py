n=int(input())
v=list(map(int,input().split()))
age=list(map(int,input().split()))
# d={}
# for i in range(n):
#     if age[i]>=18:
#         if v[i] not in d:
#             d[v[i]]=1
#         else:
#             d[v[i]]+=1
# ma=0
# ele=0
# for i in d:
#     if d[i]>ma:
#         ma=d[i]
#         ele=i
# count=0
# for i in d :
#     if d[i]==ma:
#         count+=1
# if count>1:
#     print(-1)
# else:
#     print(ele)

c=[0]*(max(v))
for i in range(n):
    if age[i]>=18:
        c[v[i]-1]+=1
m=max(c)
print(c.index(m)+1)
temp=sorted(c,reverse=True)
if temp[0]==temp[1]:
    print(-1)
else:
    print(c.index(temp[0])+1)