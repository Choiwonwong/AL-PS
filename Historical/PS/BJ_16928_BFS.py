# 100번 칸에 도착하기 위한 최솟값
# 100 * 100판 -> BFS 응용
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ladders = {} # 사다리
snakes = {} # 뱀
for _ in range(N):
    start, to = map(int, input().split())
    ladders[start] = to
for _ in range(M):
    start, to = map(int, input().split())
    snakes[start] = to

graph = [float('inf')] * (110) # 그래프 모델링
graph[0], graph[1] = 0, 0 # 초기값 갱신
visited = [False] * (110) # 방문 여부
queue = deque([1]) # 큐 선언
while queue: # BFS 탐색
    idx = queue.popleft()
    for i in range(1, 7): # 다음 위치로 가는 1 ~ 6까지 계산
        n_idx = idx + i
        if not visited[n_idx]: # 방문하지 않는 노드일 경우
            graph[n_idx] = min(graph[idx] + 1, graph[n_idx])
            if n_idx in ladders: # 사다리에 속할 경우
                # 사다리로 이동한 값과 기존 값 중 작은값으로 갱신
                graph[ladders[n_idx]] = min(graph[n_idx], graph[ladders[n_idx]])
                queue.append(ladders[n_idx])
                visited[ladders[n_idx]] = True
            elif n_idx in snakes: # 사다리에 속할 경우
                # 뱀으로 이동한 값과 기존 값 중 작은값으로 갱신
                graph[snakes[n_idx]] = min(graph[n_idx], graph[snakes[n_idx]])
                queue.append(snakes[n_idx])
                visited[snakes[n_idx]] = True
            else: # 주사위만 굴릴 경우
                queue.append(n_idx)
            visited[n_idx] = True
    if visited[100] == True:
        break
print(graph[100])



# # DP 하다가 포기
# dp = [float('inf')] * (101)
# dp[0] = 0
# dp[1] = 0


# for i in range(2, 101):
#     if i <= 6:
#         tmp = min(dp[1:i]) + 1
#     else:
#         tmp = min(dp[i-6:i]) + 1
#     dp[i] = min(tmp, dp[i])
#     if i in ladders:
#         dp[ladders[i]] = dp[i]

# for start, to in snake.items():
#     dp[to] = min(dp[start], dp[to])

# for i in range(2, 101):
#     if i <= 6:
#         tmp = min(dp[1:i]) + 1
#     else:
#         tmp = min(dp[i-6:i]) + 1
#     dp[i] = min(tmp, dp[i])
#     if i in ladders:
#         dp[ladders[i]] = dp[i]

# print(dp[100])