import sys

read=sys.stdin.readline
sco=[[0 for i in range(101)]for i in range(3)]
###print(sco)
n=int(read())
ply=[0 for i in range(n+1)]
for i in range(1,n+1):
    for j,k in enumerate(map(int,read().split())):
        if sco[j][k]!=-1 and sco[j][k]!=0:
            sco[j][k]=-1
        if sco[j][k]==0:
            sco[j][k]=i
###print(sco)

for i in range(3):
    for k,j in enumerate(sco[i]):
        if j==-1 or j==0:
            continue
        ply[j]+=k

for i in range(1,n+1):
    print(ply[i])
