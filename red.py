#minimum number of steps req to reduce a number to 1 
#If n is even reduce either by adding 1or sub 1 and if n is even reduce the number by dividing it by 2
def redu(n,steps):
    if n==1:
        return steps
    if n%2==0:
        steps+=1
        steps=redu(n//2,steps)
    else:
        a=redu(n-1,steps)
        b=redu(n+1,steps)
        steps=min(a,b)
        steps+=1
    return steps
n=int(input())  
print(redu(n,0))

# def fun(n):
#     if n==1:
#         return 0
#     elif n%2==0:
#         return 1+fun(n//2)
#     else:
#         return 1+min(fun(n-1),fun(n+1))
# fun(15)