# DP로 두칸 피보나치 문제
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    if N <= 3:
        print(1)
    else:
        dp = [1, 1, 1]
        for i in range(4, N+1):
            dp.append(dp[-2] + dp[-3])
        print(dp[-1])