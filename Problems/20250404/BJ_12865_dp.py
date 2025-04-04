# 평범한 배낭
# https://www.acmicpc.net/problem/12865
# import sys

# N, K = map(int, input().split())
# products = []
# for _ in range(N):
#     product = list(map(int, sys.stdin.readline().rstrip().split()))
#     if product[0] > K:
#         continue
#     products.append(product)

# 일단 백트래킹 한번 해볼까?
# value = []
# weight = []
# result = [0]
# visited = [False] * N
# def backtracking():
#     if sum(weight) > K:
#         temp_value = sum(value[:-1])
#         if temp_value > max(result):
#             result.append(temp_value)
#         return
        
#     for i in range(N):
#         if visited[i]:
#             continue
#         w, v = products[i]
#         weight.append(w)
#         value.append(v)
#         visited[i] = True
#         backtracking()
#         weight.pop()
#         value.pop()
#         visited[i] = False

# backtracking()
# print(max(result))

# 시간 복잡도 바로 아웃

## 투포인터 접근 해보기 -> 이론상 불가능
## 이건 DP 문제라는데,, 왜 DP일까?

# Brute Force는 불가능
# Greedy 또한 불가능 -> 물건 많이 넣기가 아니기 때문에!
## 부분 문제의 정의 가능.
## 무게 W에서의 최적해로 쪼개는 것이 가능하다. -> 이게 핵심임
## 아하! 그냥 W 배열 선언해두고, 거기에 최대값 집어넣게 만드는거구나
## 입력받은 무게에서 

# import sys

# N, K = map(int, input().split())
# dp = [0] * (K+1)
# products = []
# for _ in range(N):
#     products.append(list(map(int, sys.stdin.readline().rstrip().split())))

# # products.sort(key=lambda x : x[0], reverse=True)

# for weight in range(1, K+1):
#     for w, v in products:
#         if w > weight:
#             continue
#         dp[weight] = max(dp[weight], dp[weight-w] + v)

# print(dp)
# print(max(dp))

import sys

N, K = map(int, input().split())
dp = [0] * (K+1)
products = []
for _ in range(N):
    products.append(list(map(int, sys.stdin.readline().rstrip().split())))

for w, v in products:
    for weight in range(K, w - 1, -1): 
        dp[weight] = max(dp[weight], dp[weight - w] + v)

print(max(dp))

# DP 어렵다.. 더 공부하자!