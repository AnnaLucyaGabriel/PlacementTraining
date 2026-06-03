n=[5,4,3,2,1]
largest,second=0,0
for i in n:
    if largest<i:
        second=largest
        largest=i
    elif i>second and i!=largest:
        second=i
print(second)
