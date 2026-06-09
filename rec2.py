#1,2,3,4,5
#Head traversal
#1st entire recursion is done and then it returns back to where it was called
# def fun2(n):
#     if n==0:
#         return
#     fun2(n-1)
#     print(n)
# n=10
# fun2(10)

#10,8,6,4,3
# def fun3(n):
#     if n==0:
#         return
#     if n%2==0:
#         print(n)
#     fun3(n-1)

# fun3(10)    

#2 4 6 8 10
# def fun4(n):
#     if n==0:
#         return
#     fun4(n-1)
#     if n%2==0:
#         print(n)
# n=10
# fun4(n)


# #5 4 3 2 1 2 3 4 5 
# def fun5(n):
#     if n==0:
#         return
#     print(n,end=" ")
#     fun5(n-1)
#     if n>1:
#         print(n,end=" ")
# fun5(5)


#to print the returned value
# def fun(n):
#     if n==0:
#         return 200
#     k=fun(n-1)
#     print(n,end=" ")
#     return k
# n=5
# k=fun(n)
# print(k)

#1 2 3 4 5 4 3 2 1
def fun6(n,m=0):
    if n==m:
        return
    print(m+1,end=" ")
    fun6(n,m+1)
    if(n!=m+1):
        print(m+1,end=" ")

fun6(5)
