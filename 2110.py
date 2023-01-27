import sys
import math
read=sys.stdin.readline
n,c=map(int,read().split())
road=[]
for i in range(n):
    road.append(int(read()))
road=sorted(road)
start=1
end=(road[-1]-road[0])//(c-1)+1
print(start,end)
ans=1

while True:
    mid=(start+end)//2
    sett=road[0]
    cnt=1
    for i in road[1:]:
        if i-sett>=mid:
            cnt+=1
            sett=i
    if cnt>=c:
        ans=max(mid,ans)
        start=mid
    else:
        end=mid
    print(start,end,mid)
    if start+1==end:
        break
    
print(ans)



