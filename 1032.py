import sys
read=sys.stdin.readline
n=int(read())
if n==1:
    print(read().rstrip())
else:
    firstwd=list(map(str,read().rstrip()))    
    for i in range(n-1):
        secwd=[y if x==y else '?' for x,y in zip(list(map(str,read().rstrip())),firstwd)]
        firstwd=secwd
    print(''.join(firstwd))
