import sys
read=sys.stdin.readline
n,m,k=map(int,read().split())
#print(siz)
dp=[0 for i in range(4*n)]

def update(start,end,node,index,change):
    if (index<start) or (index>end):
        return 0
    dp[node]+=change
    if start==end:
        return 0
    mid=(start+end)//2
    update(start,mid,node*2,index,change)
    update(mid+1,end,node*2+1,index,change)

lis=[]
for i in range(n):
    num=int(read())
    lis.append(num)
    update(0,n-1,1,i,num)
print(lis)
print(dp)

def Sum(start,end,node,left,right):
    if (left>end) or (right<start):
        return 0
    if (left<=start) and (end<=right):
        return dp[node]
    mid=(start+end)//2
    return Sum(start,mid,node*2,left,right)+Sum(mid+1,end,node*2+1,left,right)

ans=[]
for i in range(m+k):
    a,b,c=map(int,read().split())
    if a==1:
        
        cha=c-lis[b-1]
        lis[b-1]=c
        update(0,n-1,1,b-1,cha)
        print(dp)
        print(lis)
    if a==2:

        print(Sum(0,n-1,1,b-1,c-1))
        ans.append(Sum(0,n-1,1,b-1,c-1))

for i in ans:
    print(i)
  
