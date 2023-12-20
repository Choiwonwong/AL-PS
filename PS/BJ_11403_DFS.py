# 인접 행렬 방식으로 간선을 입력받음

import sys
input = sys.stdin.readline

N = int(input())
maps = [list(map(int, input().rstrip().split())) for _ in range(N)]

result = []

for i in range(N):
    stack = [i]
    visited = [0] * N
    while stack:
        cur = stack.pop()
        for j in range(N): # 해당 노드에서 갈 수 있는 다음 노드 찾기
            next_node = maps[cur][j]
            if next_node == 1 and visited[j] == 0: # 간선이 존재하고, 방문하지 않은 노드일 때
                visited[j] = 1 # 방문 처리를 하고, 스택에 추가
                stack.append(j)
    result.append(visited)

for i in range(N):
    print(" ".join(list(map(str, result[i]))))