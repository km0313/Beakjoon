import sys
read=sys.stdin.readline
n,k=map(int,read().split())#n 총물건수 k 버틸수있는무게
stuff=[]#첫번째 값:무게 두번째 값:가치
for i in range(n):
    stuff.append(list(map(int,read().split())))

ans=[[0 for i in range(k+1)] for j in range(n)]
for i in range(n):
    for sm in range(1,k+1):
        if sm>=stuff[i][0]:
            ans[i][sm]=max(ans[i-1][sm],ans[i-1][sm-stuff[i][0]]+stuff[i][1])
        else:
            ans[i][sm]=ans[i-1][sm]

print(max(ans[n-1]))

