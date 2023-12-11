# BFS 수행
import sys
from collections import deque
T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(T):
    M, N, L = list(map(int, input().split()))
    maps = [[0 for _ in range(N)] for _ in range(M)]
    for _ in range(L):
        x, y = map(int, sys.stdin.readline().lstrip().split())
        maps[x][y] = 1
    
    visited = set()
    count = 0
    for i in range(M):
        for j in range(N):
            queue = deque()
            if maps[i][j] == 1 and (i, j) not in visited:
                queue.append([i, j])
                count += 1
            while queue:
                cx, cy = queue.popleft()
                if (cx, cy) not in visited:
                    visited.add((cx, cy))
                    for k in range(4):
                        nx = cx + dx[k]
                        ny = cy + dy[k]
                        if 0 <= nx < M and 0 <= ny < N:
                            if maps[nx][ny] == 1:
                                queue.append((nx, ny))
    print(count)