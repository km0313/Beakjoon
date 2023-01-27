import sys

read=sys.stdin.readline
n,k=map(int,read().split())
coin=[]
for i in range(n):
    coin.append(int(read()))
count=0
while True:
    if k==0:
        break
    count+=k//coin[-1]
    k=k%coin.pop()

print(count)
