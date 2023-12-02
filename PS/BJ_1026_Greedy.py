# 가장 큰 수 * 가장 작은 수의 합을 구하면 전역 최적해가 나온다.
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort() # 오름차순 정렬
B.sort(reverse=True) # 내림차순 정렬
result = 0
for i in range(N):
    result += A[i] * B[i] # 결과값
print(result)