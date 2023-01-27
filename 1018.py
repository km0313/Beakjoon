import sys
read=sys.stdin.readline
n,m=map(int,read().split())
ches=[]
for i in range(n):
    ches.append(list(map(lambda x: 0 if x=='W' else 1,read().rstrip())))
print(ches)    
minnum=n*m
newches=[]
def zeroone(x):
    f_0,f_1=64,64
    for i in range(64):
        
        if (i+(i//8))%2==0 and x[i]==0:
            f_0-=1
        elif (i+(i//8))%2==1 and x[i]==1:
            f_0-=1
    ###for i in range(64):
    ###    if i%2==0 and x[i]==1:
    ###        f_1-=1
    ###    elif i%2==1 and x[i]==0:
    ###        f_1-=1
    return min(f_0,(64-f_0))

score=64
for i in range(m-7):
    print(i)
    for j in range(n-7):
        for k in range(8):
            newches=newches+ches[j+k][i:i+8]
        print('newches',newches)
        score=min(score,zeroone(newches))
        print('score',score)
        newches=[]

print(score)
        
