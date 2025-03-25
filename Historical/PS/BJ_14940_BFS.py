# BFS
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
maps = []
for i in range(N):
    row = list(map(int, input().split()))
    if 2 in row:
        y = row.index(2)
        x = i
    maps.append(row)

queue = deque([[x, y, 0]])
visited = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while queue:
    cx, cy, count = queue.popleft()
    if (cx, cy) not in visited:
        visited.add((cx, cy))
        maps[cx][cy] = str(count)
        for i in range(4):
            nx = dx[i] + cx
            ny = dy[i] + cy
            if 0 <= nx < N and 0 <= ny < M:
                if maps[nx][ny] == 1:
                    queue.append([nx, ny, count + 1])
for i in range(N):
    for j in range(M):
        if (i, j) not in visited:
            maps[i][j] = '0' if maps[i][j] == 0 else '-1'
            
for i in range(N):
    print(" ".join(maps[i]))