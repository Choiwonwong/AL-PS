# BFS 수행
# 모든 1로부터 시작한 BFS 탐색 수행
# 모든 노드를 탐색할 때 까지 걸리는 최소 시간 반환하면 됨
# 탐색 후 -1을 제외한 노드의 수와 전체 노드의 수 - 방문한 노드가 같지 않으면 도달 못함 -> -1 반환
from collections import deque # queue 자료형 사용
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
queue = deque([])
visited = set() # 방문한 노드 자료형
disable_node_count = 0 # 방문하지 못하는 노드의 수
days = 0 # 결과
graph = [] # 그래프 자료형
for i in range(N):  # 그래프 생성
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 1:
            queue.append([i, j, 0]) # 출발지점 큐에 push
        elif row[j] == -1: 
            disable_node_count += 1 # Block 지점 개수 Count
    graph.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y, count = queue.popleft()
    if (x, y) in visited:
        continue
    days = max(days, count)
    visited.add((x, y))
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append([nx, ny, count + 1])
if len(visited) == (N * M - disable_node_count):
    print(days)
else:
    print(-1)