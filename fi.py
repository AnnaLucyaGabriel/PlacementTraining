#to find the maximum no of elements with which the sum doesn't go beyoind k
l1=list(map(int,input().split()))
k=int(input())
r=0;l=0;m=0;s=0
while(r<len(l1)):
    s+=l1[r]
    while(s>k):
        s-=l1[l]
        l+=1
    l2=r-l+1
    m=max(m,l2)
    r+=1
print(m)
