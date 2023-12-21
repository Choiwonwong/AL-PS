# DFS로 구현하고
# 좌표가 갖는 값을 갖고 노는 문제이다.

import sys
input = sys.stdin.readline

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
visited1 = [[False] * N for _ in range(N)]
visited2 = [[False] * N for _ in range(N)]
count1, count2 = 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N):
    for j in range(N):
        if visited1[i][j]:
            continue
        stack = [(i, j)]
        cur_type = graph[i][j]
        count1 += 1
        while stack:
            x, y = stack.pop()
            visited1[x][y] = True
            for k in range(4):
                nx = x + dx[k] 
                ny = y + dy[k] 
                if 0 <= nx < N and 0 <= ny < N:
                    if graph[nx][ny] == cur_type and not visited1[nx][ny]:
                        stack.append((nx, ny))
for i in range(N):
    for j in range(N):
        if visited2[i][j]:
            continue
        stack = [(i, j)]
        if graph[i][j] in ["G", "R"]:
            cur_type = ["G", "R"]
        else:
            cur_type = ["B"]
        count2 += 1
        while stack:
            x, y = stack.pop()
            visited2[x][y] = True
            for k in range(4):
                nx = x + dx[k] 
                ny = y + dy[k] 
                if 0 <= nx < N and 0 <= ny < N:
                    if graph[nx][ny] in cur_type and not visited2[nx][ny]:
                        stack.append((nx, ny))
print(count1, count2)