import sys
import math
read=sys.stdin.readline
minn,maxx=map(int,read().split())
point=math.ceil(maxx**(1/2))
dp=[True for i in range(maxx-minn+1)]#시작점 0 index값=minn값, dp.index+minn 으로 출발

for i in range(2,point+1):
    countmax=(maxx//(i*i))
    countmin=math.ceil(minn/(i*i))
    for k in range(countmin,countmax+1):
        dp[k*i*i-minn]=False
ans=0
for i in range(len(dp)):
    if dp[i]==True:
        print(i+minn)
        ans+=1
print(ans)