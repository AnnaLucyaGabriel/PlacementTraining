n=int(input())
flag=1
if n==2:
    print("Prime")
elif n==1:
    print("Not Prime")
else:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            flag=0
            break
    if flag==1:
        print("Prime")
    else:
        print("Not prime")
