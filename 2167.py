import sys

ari=[]
n,m=map(int,sys.stdin.readline().split())

for i in range(n):
    ari.append(list(map(int,sys.stdin.readline().split())))
    

print(ari)
count=int(sys.stdin.readline())
sumari=[]

for i in range(count):
    sumraw=0
    i,j,x,y=map(int,sys.stdin.readline().split())
    for k in range(i,x+1):
        sumraw+=sum(ari[k-1][j-1:y])
    sumari.append(sumraw)
    

for i in range(count):
    print(sumari[i])
