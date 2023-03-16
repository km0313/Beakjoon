import sys
import math

read=sys.stdin.readline
n=int(read())
lis=list(map(int,read().split()))
print(n,lis)
dp=[math.inf]+lis
for i in range(2,n+1):
    for j in range(1,i//2+1):
        dp[i]=min(dp[i],dp[j]+dp[i-j])
print(dp)