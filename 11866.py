import sys
read=sys.stdin.readline
n,k=map(int,read().split())
ysp=[i for i in range(1,n+1)]
count=-1
new_ysp=[]
while True:
    if len(ysp)==0:
        break
    count=(count+k)%n
    new_ysp.append(ysp.pop(count))
    count-=1
    n-=1

print('<',', '.join(map(str,new_ysp)),'>',sep='')
