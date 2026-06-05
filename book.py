k=int(input())
arr=list(map(int,input().split()))
su=sum(arr[:k])
ma=su
# for i in range(len(arr)-k):
#     su=0
#     for j in range(i,i+k):
#         su+=arr[j]
#     ma=max(ma,su)
for i in range(1,len(arr)-k+1):
    su=su-arr[i-1]+arr[i+k-1]
    ma=max(ma,su);
print(ma)