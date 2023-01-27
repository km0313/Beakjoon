import sys

read=sys.stdin.readline
n=int(read())
l=list(map(int,read().split()))
print(l)
print(max(l))
dp=[[0 for i in range(max(l)+1)]for k in range(len(l)+1)]
for i in range(len(l)):
    dp[i][l[i]]=1
answer=0
for k in range(len(l)):
    for i in range(max(l)+1):
        if l[k]<i:
            dp[k+1][l[k]]=max(dp[k][i]+1,dp[k+1][l[k]])
            
            '''
            if dp[k+1][l[k]]==dp[k][i]+1:
                print(k,l[k],i,dp[k][i]+1)
            '''
        dp[k+1][i]=max(dp[k][i],dp[k+1][i])
        '''
        if dp[6][10]==2:
            print(k,l[k],i)
        '''
        
    
    


    

print(dp)
print(max(dp[-1]))    

