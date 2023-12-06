# 구현 & 수학
# 유클리드 호제법 사용
N, M = map(int, input().split())
A, B = max(N, M), min(N, M)
R = 1
while R != 0:
    R = A % B
    A = B
    B = R
print(A)
print(N * M // A)