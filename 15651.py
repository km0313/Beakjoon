import sys
read=sys.stdin.readline
n,m=map(int,read().split())
resul=[[] for i in range(m)]
counting=[i for i in range(1,n+1)]

for i in range(1,m+1): #1~3(첫째자리 둘째자리 셋째자리)
     #3^3의 수들을
    for j in range(n**i):#첫째자리는 27/3개의 같은수 둘째자리는 9/3~ 셋째자리는 3/3~
        for k in range(1,n**(m-i)+1):
            resul[i-1].append(counting[j%n])
ans=[]
for i in range(n**m):
    for k in range(m):
        ans.append(resul[k][i])
    print(*ans)
    ans.clear()

    

    


    