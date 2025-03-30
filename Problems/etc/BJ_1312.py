import sys
input = sys.stdin.readline

A, B, N = map(int, input().split())
for i in range(N):
    A = (A%B) * 10
    result = A // B
print(result)
# decimal_part = str(float(A) / B).split('.')[1] 
# if N <= len(decimal_part):
#     print(int(decimal_part[N-1]))  # N번째 자리수를 반환
# else:
#     print(0)  # N이 소숫점 아래 자릿수보다 큰 경우, -1을 반환