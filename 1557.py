import sys
import math
arr=[0 for i in range(42001)]
arr[1]=1

for i in range(1,42001):
    for k in range(2*i,42001,i):
        arr[k]-=arr[i]

read=sys.stdin.readline
maxx=int(read())
point=math.ceil((2*maxx)**(1/2))
#dp=[True for i in range(2*maxx)]시작점 0 index값=minn값, dp.index+minn 으로 출발
start=0
end=2*maxx
while True:
    if start+1>=end:
        break
    mid=(start+end)//2
    
    count=0
    sqr=int(mid**(0.5))
    for i in range(1,sqr+1):
        count+=arr[i]*(mid//(i*i))
    
    if count<maxx:
        start=mid
    else:
        end=mid

print(end)
