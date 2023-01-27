from cmath import inf

#problem=[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]
problem=[[20, 10, 2, 0, 1]]
###problem=[[10,15,2,1,2],[20,20,3,3,4]]
alp=10
cop=10
dp=[]
def solution(alp, cop, problems):
    global dp
    maxcop_req=sorted(problems, key=lambda x:x[1])[-1][1]
    problems=sorted(problems)
    maxalp_req=problems[-1][0]
    answer=0
    dp=[[]for i in range(maxalp_req+1)]
    for i in range(maxalp_req+1):
        for k in range(maxcop_req+1):
            dp[i].append(max(0,i-alp)+max(0,k-cop))
    
   
    for k in range(cop,maxcop_req+1):
        for i in range(alp,maxalp_req+1):
            for prob in problems:
                if i>=prob[0] and k>=prob[1]:
                    dp[i][k]=min(dp[i][k],dp[max(i-prob[2],alp)][max(k-prob[3],cop)]+prob[4])
            
                    
    answer=dp[maxalp_req][maxcop_req]
    return answer

print(solution(alp, cop, problem))
print(dp)
#print(dp[10][10],dp[10][15],dp[12][16],dp[14][17],dp[16][18],dp[18][19],dp[20][20])
#print(dp[2][1],dp[4][2],dp[4][5],dp[7][6],dp[10][7],dp[10][11])