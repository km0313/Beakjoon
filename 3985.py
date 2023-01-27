import sys
read=sys.stdin.readline
n=int(read())
cake=[0 for i in range(n)]
k=int(read())
guest=[]
for i in range(k):
    guest.append(list(map(int,read().split())))

expecguest=0
expecnum=0
for i in reversed(range(k)):
    count=guest[i][1]-guest[i][0]
    cake[guest[i][0]-1:guest[i][1]]=[i+1 for k in range(count+1)]
    ###print(expecguest,count)
    if expecguest <= count:
        expecnum=i+1
        expecguest=count
        ###print(expecnum)
    ###print(guest[i])
    ###print(cake)
###print(cake)
print(expecnum)
print(max(filter(lambda x: x!=0,cake), key=cake.count))    
    
