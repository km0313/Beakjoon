import sys
from collections import deque

read=sys.stdin.readline
col,ral=map(int,read().split())
stock=deque([[-1 for i in range(col+2)]])

for i in range(ral):
    stock.append([-1]+list(map(int,read().split()))+[-1])
stock.append([-1 for i in range(col+2)])

###print(stock)
first_check=0
for rl in range(1,ral+1):
    if 0 in stock[rl]:
        first_check+=1
if first_check==0:
    print(0)
    exit(0)
new_counting=0
counting=0
ripe=deque()
for i in range(1,ral+1):
    for k in range(1,col+1):
        if stock[i][k]==1:
            if stock[i+1][k]==0:
                ripe.append([i+1,k])
                counting+=1
            if stock[i][k+1]==0:
                ripe.append([i,k+1])
                counting+=1
            if stock[i-1][k]==0:
                ripe.append([i-1,k])
                counting+=1
            if stock[i][k-1]==0:
                ripe.append([i,k-1])
                counting+=1
for i,k in ripe:
    stock[i][k]=1                
days=1
###print(stock)
###print(ripe)
if new_counting==counting:
    print(-1)
else:
    new_counting=counting
    while True:
        new_ripe=deque()
        for i,k in ripe:
            if stock[i+1][k]==0:
                
                new_ripe.append([i+1,k])
                counting+=1
                stock[i+1][k]=1
            if stock[i][k+1]==0:
                
                new_ripe.append([i,k+1])
                counting+=1
                stock[i][k+1]=1
            if stock[i-1][k]==0:
                
                new_ripe.append([i-1,k])
                counting+=1
                stock[i-1][k]=1
            if stock[i][k-1]==0:
               
                new_ripe.append([i,k-1])
                counting+=1
                stock[i][k-1]=1
        
        if new_counting==counting:
            second_check=0
            for rl in range(1,ral+1):
                if 0 in stock[rl]:
                    second_check+=1
            if second_check!=0:
                print(-1)
                exit(0)
            print(days)
            break
        days+=1 
        new_counting=counting
        ripe=new_ripe
        '''print(new_counting)
        print(stock)
        print('')
        print(ripe)'''
