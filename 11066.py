from cmath import inf
import sys
read=sys.stdin.readline
n=int(read())
result=[]
for i in range(n):
    num=int(read())
    dp=[[0 for i in range(num+1)] for k in range(num+1)]
    
    marking=[]
    chap=[0]+list(map(int,read().split()))
    Sum=chap
    for i in range(1,num):
        Sum[i+1]+=Sum[i]
    print(Sum)
    for i in range(1,num+1):
        for j in range(1,num-i+1):
            dp[j][i+j]=inf
            for k in range(j,i+j):
                print(j,i+j)
                dp[j][i+j]=min(dp[j][i+j],dp[j][k]+dp[k+1][i+j]+Sum[i+j]-Sum[j-1])
    result.append(dp[1][num])
for i in result:
    print(i)
    









