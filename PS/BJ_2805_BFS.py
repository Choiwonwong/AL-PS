N = int(input())
maps = []
for _ in range(N):
    maps.append(list(input()))

number = 0
counts = []
visited = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N):
    for j in range(N):
        if maps[i][j] == '1' and (i, j) not in visited:
            number += 1
            count = 0
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                if (x, y) not in visited:
                    visited.add((x, y))
                    count += 1
                    for idx in range(4):
                        nx, ny = dx[idx] + x, dy[idx] + y
                        if 0 <= nx < N and 0 <= ny < N:
                            if maps[nx][ny] == '1':
                                stack.append((nx, ny))
            counts.append(count)
print(number)
counts.sort()
for c in counts:
    print(c)