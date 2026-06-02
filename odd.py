l=input().split()
r=[]
for i in l:
    count=l.count(i)
    if count%2!=0 and i not in r:
        r.append(i)
print(r)