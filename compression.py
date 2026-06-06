a=input()
res=""
k=0
# for i in range(len(a)):
count=1
#     while(l<=e):
#         if a[l]==a[e]:
#             e+=1
#             count+=1
#         else:
#             break
#     print(b)
for i in range(1,len(a)):
    if a[k]==a[i]:
        count+=1
    else:
        res+=a[i-1]+str(count)
        k=i
        count=1
    
res+=a[-1]+str(count)
print(res)  