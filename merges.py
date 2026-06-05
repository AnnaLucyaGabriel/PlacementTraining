l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
# l3=l1+l2
# l3.sort()
# print(l3)
i=0;j=0
while i<len(l1) and j<len(l2):
    if l1[i]<l2[j]:
        l3.append(l1[i])
        i+=1
    else:
        l3.append(l2[j])
        j+=1
if i<len(l1):
    for i in range(i,len(l1)):
        l3.append(l1[i])
        i+=1
if j<len(l2):
    for i in range(j,len(l2)):
        l3.append(l2[j])
        j+=1
print(l3)