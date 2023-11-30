# 매번 부분합을 구해야함.
# 항상 가장 작은 값을 선택하면 됨.
N = int(input())
arr = list(map(int, input().split()))
result = 0
arr.sort()
for i in range(N):
    result += arr[i] # 현재 사람이 걸리는 시간
    result += sum(arr[:i]) # 현재 사람이 기다리는 시간
print(result)