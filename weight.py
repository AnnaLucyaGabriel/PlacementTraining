#791A codeforces
li,bu=map(int,input().split())
year=0
while li<=bu:
    year+=1
    li*=3
    bu*=2
print(year)