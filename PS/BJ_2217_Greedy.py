N = int(input())
ropes = []
for _ in range(N):
    ropes.append(int(input()))
ropes.sort(reverse=True)
weights = 0
for idx in range(len(ropes)):
    weights = max(weights, ropes[idx] * (idx + 1))
print(weights) # 중량의 최대값을 항상 살핀다.