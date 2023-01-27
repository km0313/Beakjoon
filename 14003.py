import sys
import math
read=sys.stdin.readline
n=int(read())
l=list(map(int,read().split()))
l=l
leng=len(l)
dp=[0 for i in range(leng)]
dpcount=[0]+[math.inf for i in range(leng)]
'''
for i in range(len(l)):
    for k in range(i):
        if l[k]<l[i]:
            dp[i]=max(dp[i],dp[k]+1)
ans=max(dp)
'''
for i in range(leng):
    start=0
    end=leng
    while True:
        if start+1==end:
            dpcount[end]=l[i]
            dp[i]=end
            break
        mid=(start+end)//2
        if dpcount[mid]<l[i]:
            start=mid
        else:
            end=mid

#print(dp)
#print(dpcount)
ans=max(dp)
answ=ans
lis=[]

for i in range(leng-1,-1,-1):
    if dp[i]==ans:
        lis.append(l[i])
        ans-=1
        if ans==0:
            break
#print(dp)
#print(max(dp))
print(answ)
print(*lis[::-1])
