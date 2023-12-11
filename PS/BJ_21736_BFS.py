from collections import deque
N, M = map(int, input().split())
maps = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if maps[i][j] == 'I':
            start = [i, j]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque([start])
visited = set()
count = 0
while queue:
    x, y = queue.popleft()
    if (x, y) not in visited:
        if maps[x][y] == 'P':
            count += 1
        visited.add((x, y))
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < M:
                if maps[nx][ny] != 'X':
                    queue.append([nx, ny])
print(count if count > 0 else "TT")
