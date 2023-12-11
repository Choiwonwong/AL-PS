# DFS 사용
import sys
V = int(input())
E = int(input())
edges = {1:[]} # V = 0 예외처리
for _ in range(E):
    fr_v, to_v = map(int, sys.stdin.readline().rstrip().split())
    if fr_v not in edges:
        edges[fr_v] = [to_v]
    else:
        edges[fr_v].append(to_v)
    if to_v not in edges:
        edges[to_v] = [fr_v]
    else:
        edges[to_v].append(fr_v)
stack = []
visited = set()
stack.append(1)
while stack:
    cur = stack.pop()
    if cur not in visited:
        visited.add(cur)
        stack.extend(edges[cur])
print(len(visited)-1)