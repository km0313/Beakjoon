from cmath import inf

problem=[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]
#problem=[[10,15,2,1,2],[20,20,3,3,4]]
alp=0
cop=0

dp=[]
def solution(alp, cop, problems):
    global dp
    maxcop_req=max([i[1] for i in problems])
    maxalp_req=max([i[0] for i in problems])
    problems=sorted(problems)
    answer=0
    dp=[[]for i in range(maxalp_req+1)]
    for i in range(maxalp_req+1):
        for k in range(maxcop_req+1):
            dp[i].append(max(0,i-alp)+max(0,k-cop))
    
    if maxalp_req <= alp:
        alp = maxalp_req
    if maxcop_req <= cop:
        cop =maxcop_req
    for k in range(cop,maxcop_req+1):
         for i in range(alp,maxalp_req+1):
            for prob in problems:
                if i>=prob[0] and k>=prob[1]:
                    m=i
                    n=k
                    newm=min(prob[2]+m,maxalp_req)
                    newn=min(prob[3]+n,maxcop_req)
                    dp[newm][newn]=min(dp[newm][newn],dp[min(m,maxalp_req)][min(n,maxcop_req)]+prob[4])
            
                    
    answer=dp[-1][-1]
    return answer

print(solution(alp, cop, problem))
print(dp)
#print(dp[10][10],dp[10][15],dp[12][16],dp[14][17],dp[16][18],dp[18][19],dp[20][20])
print(dp[2][1],dp[4][2],dp[4][5],dp[7][6],dp[10][7],dp[10][11])

'''
def solution(alp, cop, problems):
    global dp
    maxcop_req=max([i[1] for i in problems])
    maxalp_req=max([i[0] for i in problems])
    problems=sorted(problems)
    answer=0
    dp=[[]for i in range(maxalp_req+1)]
    for i in range(maxalp_req+1):
        for k in range(maxcop_req+1):
            dp[i].append(max(0,i-alp)+max(0,k-cop))
    
    
    for k in range(0,maxcop_req+1):
         for i in range(0,maxalp_req+1):
            for prob in problems:
                if i>=prob[0] and k>=prob[1]:
                    m=i
                    n=k
                    newm=min(prob[2]+m,maxalp_req)
                    newn=min(prob[3]+n,maxcop_req)
                    dp[newm][newn]=min(dp[newm][newn],dp[min(m,maxalp_req)][min(n,maxcop_req)]+prob[4])
            
                    
    answer=dp[maxalp_req][maxcop_req]
    return answer
'''