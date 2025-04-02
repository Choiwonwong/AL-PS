# 트리의 부모 찾기 11725
## https://www.acmicpc.net/problem/11725


## 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.
## 1번 부터 N번까지인 듯

from collections import defaultdict, deque
import sys

N = int(input())
graph = defaultdict(list)
result = [None] * (N + 1)

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([[1, None]])

while queue:
    current, parent = queue.popleft()
    neighbors = graph[current]
    for neighbor in neighbors:
        if result[neighbor] is None:
            result[neighbor] = current
            queue.append([neighbor, current])
        
for i in range(2, N+1):
    print(result[i])
