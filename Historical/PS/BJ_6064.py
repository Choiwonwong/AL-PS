# 중국인 나머지 정리
import math
import sys
input = sys.stdin.readline

def find_k(M, N, x, y):
    lcm = M * N // math.gcd(M, N)
    current_year = x
    for _ in range(lcm // M):
        if (current_year - 1) % N + 1 == y:
            return current_year
        current_year += M
    return -1


T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    result = find_k(M, N, x, y)
    print(result)