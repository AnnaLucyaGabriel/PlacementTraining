n=int(input())
rev=0
count=0
org=n
while(n>0):
    n=n//10
    count+=1
n=org
while(n>0):
    rem=n%10
    rev+=rem**count
    n=n//10
if org==rev:
    print("Armstrong")
else:
    print("Not Armstrong")