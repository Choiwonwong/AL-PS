# BFS
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = {} # 그래프 모델 구현 - 딕셔너리로
for _ in range(M): 
    start, end = map(int, input().split())
    if start not in graph:
        graph[start] = [end]
    else:
        graph[start].append(end)
    if end not in graph:
        graph[end] = [start]
    else:
        graph[end].append(start)

kb_scores = []
people = sorted(list(graph.keys())) # 사람들 수 배열 생성
for person in people: # 모든 사람의 KB 값을 계산
    visited = set()
    queue = deque([[person, 0]])
    score = 0
    while queue:
        cur, count = queue.popleft()
        if cur not in visited:
            visited.add(cur)  # 방문할 때 KB_Score 추가
            score += count
            for next_person in graph[cur]: # 다음 노드 추가
                if next_person not in visited:
                    queue.append([next_person, count + 1])
    kb_scores.append(score)
print(people[kb_scores.index(min(kb_scores))])