#Tail recursion
#5 4 3 2 1
def fun1(n):
    if n==0:
        return 
    print(n)
    fun1(n-1)
n=10
fun1(10)