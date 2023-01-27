import sys
n=int(sys.stdin.readline())
ches=[0]*n

ans=0
def ispossible(x):
    for i in range(x):
        if ches[x]==ches[i] or abs(ches[x]-ches[i])==abs(x-i):
            return False
    return True    

def nqueen(k,num=n):
    global ans
    if k==num:
        ans+=1
        return 0
    else:
        for i in range(1,num+1):
            ches[k]=i
            if ispossible(k):
                nqueen(k+1)
for i in range(1,(n+1)//2):
    ches[0]=i
    nqueen(1)
    ches=[0]*n
print(ans)




