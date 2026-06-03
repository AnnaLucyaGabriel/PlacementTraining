l=[1,3,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,2,2,2,2,4,4,4,4,4,4,4,4]
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
ma=0
ele=0
for i in d:
    if d[i]>ma:
        ma=d[i]
        ele=i
print(ele)