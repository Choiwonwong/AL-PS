import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * 3 for _ in range(N)] # dp[i][j]: i번째 열의 j번째 스티커를 선택했을 때의 최대 점수
    dp[0][0] = stickers[0][0]
    dp[0][1] = stickers[1][0]
    dp[0][2] = 0

    for i in range(1, N):
        dp[i][0] =  max(dp[i - 1][1], dp[i - 1][2]) + stickers[0][i]
        dp[i][1] =  max(dp[i - 1][0], dp[i - 1][2]) + stickers[1][i]
        dp[i][2] =  max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
        
    print(max(dp[N-1][0], dp[N-1][1], dp[N-1][2]))


# import sys
# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     N = int(input())
#     stickers = [list(map(int, input().split())) for _ in range(2)]

#     dpUp = [0] * N
#     dpDown = [0] * N

#     dpUp[-1] = stickers[0][-1]
#     dpDown[-1] = stickers[1][-1]
#     flag = 0
#     for i in range(N-1, 0, -2):
#         empty = stickers[1][i-2] if flag == 0 else stickers[0][i-2]
#         notEmpty = stickers[1][i-1] + stickers[0][i-2] if flag == 0 else stickers[0][i-1] + stickers[1][i-2]

#         if empty > notEmpty:
#             dpUp[i-2] = stickers[1][i-2] if flag == 0 else stickers[0][i-2]
#             flag = 1 if flag == 0 else 0
#         else:
#             dpUp[i-1] = stickers[1][i-2] if flag == 0 else stickers[0][i-2]
#             dpUp[i-2] = stickers[0][i-2] if flag == 0 else stickers[1][i-2]
#             flag = 0 if flag == 0 else 1
#     print(dpUp)