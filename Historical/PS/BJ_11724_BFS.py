# BFS

import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
if M == 0:
    print(N)
    exit(0)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
visited = [False] * (N+1)
result = 0
for i in range(1, len(graph)):
    if not visited[i]:
        result+=1
        queue = deque([i])
        while queue:
            cur = queue.popleft()
            if not visited[cur]:
                visited[cur] = True
                queue.extend(graph[cur])
print(result)

## 노드에 대한 고려가 이루어지지 않음.
# import sys
# from collections import deque
# input = sys.stdin.readline
# N, M = map(int, input().split())
# if M == 0:
#     print(N)
#     exit(0)
# graph = {}
# for _ in range(M):
#     start, end = map(int, input().split())
#     if start not in graph:
#         graph[start] = [end]
#     else:
#         graph[start].append(end)
#     if end not in graph:
#         graph[end] = [start]
#     else:
#         graph[end].append(start)
# visited = set()
# result = 0
# for i in graph:
#     if i not in visited:
#         result+=1
#         queue = deque([i])
#         while queue:
#             cur = queue.popleft()
#             if cur not in visited:
#                 visited.add(cur)
#                 queue.extend(graph[cur])
# print(result)