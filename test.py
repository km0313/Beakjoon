from cmath import inf
import sys

read=sys.stdin.readline
n=int(read())
m=int(read())
Iresult=[]
count=0
def IOtest(x):
    global count
    global result
    x=str(x)
    if x=='I':
        Iresult.append(count)
    
    count+=1
    return x

s=list(map(IOtest,read().rstrip()))
count=0
if len(Iresult)==0:
    print(0)
    exit(0)
prenum=inf
ans=0
for i in Iresult:
    if (prenum+2)==i:
        count+=1
        prenum=i
    else:
        ans+=max((count-n+1),0)
        count=0
        prenum=i
print(ans)