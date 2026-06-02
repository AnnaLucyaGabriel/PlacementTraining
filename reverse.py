n=int(input())
k=0
while n>0:
    r=n%10
    k=k*10+r
    n=n//10
print(k)