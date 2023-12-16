# 피보나치 수열 확장
import sys
input = sys.stdin.readline

N = int(input())
if N == 1:
    print(1)
elif N == 2:
    print(3)
else:
    n2 = 1
    n1 = 3
    result = 0
    for _ in range(2, N):
        result = n1 + 2 * n2
        n2 = n1
        n1 = result
    print(result % 10007)