import sys

input = sys.stdin.readline
INF = int(1e10)

T = int(input())
for t in range(T):
    N = int(input())
    file = [0] + list(map(int, input().split()))
    sum_file = file
    for i in range(1, N):
        sum_file[i+1] += sum_file[i]

    K = [[0] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        K[i][i] = i

    dp = [[0] * (N+1) for _ in range(N+2)]
    for i in range(1, N):
        for j in range(1, N-i+1):
            dp[j][i+j] = INF
            for k in range(K[j][i+j-1], K[j+1][i+j]+1):
                print(K[j][i+j-1], K[j+1][i+j]+1)
                temp = dp[j][k] + dp[k+1][i+j] + sum_file[i+j] - sum_file[j-1]
                if temp < dp[j][i+j]:
                    dp[j][i+j] = temp
                    K[j][i+j] = k
    print(dp[1][N])