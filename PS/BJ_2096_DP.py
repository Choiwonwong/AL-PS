# # BFS로 풀이

# from collections import deque
# import sys
# input = sys.stdin.readline

# N = int(input())
# stairs = [list(map(int, input().split())) for _ in range(N)]

# min_result = []
# for start in range(3):
#     queue = deque()
#     queue.append((stairs[0][start], start, 0))
#     while queue:
#         result, place, depth = queue.popleft()
#         for i in range(3):
#             if place == 0:
#                 if i == 2:
#                     continue
#             if place == 2:
#                 if i == 0:
#                     continue
#             if depth + 1 < N:
#                 queue.append((result + stairs[depth + 1][i], i, depth + 1))
#             else:
#                 min_result.append(result)
                
# print(max(min_result), min(min_result))
# # 메모리 초과 - 답은 맞음

# DP 사용

# import sys
# input = sys.stdin.readline

# N = int(input())
# initial = list(map(int, input().split()))

# min_dp = [[0] * 3 for _ in range(N)]
# max_dp = [[0] * 3 for _ in range(N)]

# min_dp[0] = initial.copy()
# max_dp[0] = initial.copy()

# for i in range(1, N):
#     stair = list(map(int, input().split()))
#     min_dp[i][0] = min(min_dp[i-1][0], min_dp[i-1][1]) + stair[0]
#     min_dp[i][1] = min(min_dp[i-1]) + stair[1]
#     min_dp[i][2] = min(min_dp[i-1][1], min_dp[i-1][2]) + stair[2]

#     max_dp[i][0] = max(max_dp[i-1][0], max_dp[i-1][1]) + stair[0]
#     max_dp[i][1] = max(max_dp[i-1]) + stair[1]
#     max_dp[i][2] = max(max_dp[i-1][1], max_dp[i-1][2]) + stair[2]
    
# print(max(max_dp[N-1]), min(min_dp[N-1]))

import sys
input = sys.stdin.readline

N = int(input())
initial = list(map(int, input().split()))

min_dp = initial.copy()
max_dp = initial.copy()

for _ in range(1, N):
    stair = list(map(int, input().split()))
    min_tmp = [
                min(min_dp[0], min_dp[1]) + stair[0], 
                min(min_dp) + stair[1], 
                min(min_dp[1], min_dp[2]) + stair[2]
               ]
    min_dp[0] = min_tmp[0] 
    min_dp[1] = min_tmp[1] 
    min_dp[2] = min_tmp[2] 

    max_tmp = [
                max(max_dp[0], max_dp[1]) + stair[0], 
                max(max_dp) + stair[1], 
                max(max_dp[1], max_dp[2]) + stair[2]
               ]
    max_dp[0] = max_tmp[0] 
    max_dp[1] = max_tmp[1] 
    max_dp[2] = max_tmp[2] 
    
print(max(max_dp), min(min_dp))

# 메모리 절약!!