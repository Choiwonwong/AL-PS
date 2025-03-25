# 계단은 한 번에 하나 or 두 칸
# 연속된 세 개의 계단은 밟으면 안됨
# 마지막 도착 계단은 필수
import sys
N = int(input())
stairs = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
if N == 1:
    print(stairs[0])
elif N == 2:
    print(stairs[0] + stairs[1])
else:
    dp = [0 for _ in range(N)]
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    for i in range(2, N):
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])
    print(dp[-1])