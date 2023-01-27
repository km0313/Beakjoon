import sys

read=sys.stdin.readline
n=int(read())
l=list(map(int,read().split()))
dplis=[[] for i in range(max(l)+1)]
dp=[[0 for i in range(max(l)+1)]for k in range(len(l)+1)]
for i in range(len(l)):
    dp[i][l[i]]=1
answer=0
for k in range(len(l)):
    for i in range(1,max(l)+1):
        if l[k]>i:
            if dp[k][i]+1>dp[k+1][l[k]]:
                dp[k+1][l[k]]=dp[k][i]+1
                dplis[i].append(l[k])
                print(l[k],i)
            else:
                dp[k+1][l[k]]=dp[k+1][l[k]]    
        dp[k+1][i]=max(dp[k][i],dp[k+1][i])
lis=[]
ans=max(dp[-1])
count=1
ran=max(l)
for i in range(ran+1):
    if dp[-1][i]==count:
        lis.append(i)
        count+=1
        if ans<count:
            break
print(dplis)        
print(dp)
print(max(dp[-1]))
print(*lis)