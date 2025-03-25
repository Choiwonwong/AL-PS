from collections import deque

N, E, S = map(int, input().split())
nodes = set() # 인접 리스트 관리 집합 자료형
maps = {} # 인접 리스트 간선 정보 저장
for _ in range(E):
    n1, n2 = map(int, input().split())
    if n1 not in nodes:
        nodes.add(n1)
        maps[n1] = [n2]
    else:
        maps[n1].append(n2)
    if n2 not in nodes:
        nodes.add(n2)
        maps[n2] = [n1]
    else:
        maps[n2].append(n1)

if S not in nodes: # 만약, 시작 정점과 연결된 간선이 없을 때 예외처리
    maps[S] = [S]

stack = [S] # DFS Stack
dfs_visited = set() # 방문 노드
while stack:
    current = stack.pop()
    if current not in dfs_visited:
        print(current, end= " ")
        dfs_visited.add(current)
        stack.extend(sorted(maps[current], reverse=True)) # 역정렬을 취해 낮은 정점 선택
print("")

queue = deque([S]) # BFS Stack
bfs_visited = set()
while queue:
     current = queue.popleft()
     if current not in bfs_visited:
        print(current, end= " ")
        bfs_visited.add(current)
        queue.extend(sorted(maps[current])) # 정렬을 취해 낮은 정점 선택