# DP
# 아래층부터 구하면서 올라가기
T = int(input())
for _ in range(T):
    K = int(input())
    N = int(input())
    dp = [[0 for _ in range(N)] for _ in range(K+1)]
    dp[0] = [i+1 for i in range(N)]
    for i in range(1, K+1):
        for j in range(N):
            dp[i][j] = sum(dp[i-1][:j+1])
    print(dp[K][N-1])