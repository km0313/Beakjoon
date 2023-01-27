import sys
read=sys.stdin.readline
n=int(read())
l=list(map(int,read().split()))
l=[0]+l
dp=[0 for i in range(len(l))]

for i in range(len(l)):
    for k in range(i):
        if l[k]<l[i]:
            dp[i]=max(dp[i],dp[k]+1)
ans=max(dp)

lis=[]

for i in range(len(dp)-1,-1,-1):
    if dp[i]==ans:
        lis.append(l[i])
        ans-=1
        if ans==0:
            break
print(dp)
print(max(dp))
print(*lis[::-1])


