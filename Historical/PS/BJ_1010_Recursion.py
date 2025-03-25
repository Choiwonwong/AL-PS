import sys
input = sys.stdin.readline

def fact(N):
    if N <= 1:
        return 1
    return N * fact(N-1)

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(fact(M) // (fact(N) * fact(M-N)))