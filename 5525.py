from cmath import inf
import sys
import re
read=sys.stdin.readline
n=int(read())
m=int(read())
Iresult=[]
Oresult=[]

count=0


def IOtest(x):
    global count
    global result
    x=str(x)
    if x=='I':
        Iresult.append(count)
    else:
        Oresult.append(count)
    count+=1
    return x

s=list(map(IOtest,read().replace('II','IOOI').split('OO')))
print(s)
print(Iresult)
print(Oresult)
print(Iresult[1:])
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
        print('count',count)
        ans+=max((count-n+1),0)
        count=0
        prenum=i
        print(prenum)
ans+=max((count-n+1),0)
print(ans)



'''
pattern='IO'
s=re.sub(pattern,'A',read().rstrip())
print(s)
pattern='AO'
s=re.sub(pattern,'O',s)
print(s)
pattern='I'
s=re.sub(pattern,'IO',s)
print(s)
pattern='AI'
s=re.sub(pattern,'A',s)
print(s)
pattern='I'
s=re.sub(pattern,'O',s)
n_s=list(filter(lambda x:x!='',s.split('O')))

for i in n_s:
    if len(i)>=n:
        count+=(len(i)-n+1)
print(count)
'''




