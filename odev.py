l=list(map(int,input().split()))
l.sort()
r=[]
for i in l:
    if i%2!=0:
        r.append(i)
    else:
        r.insert(0,i)
print(r)
