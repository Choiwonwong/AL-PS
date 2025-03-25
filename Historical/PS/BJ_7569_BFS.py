# BFS - Only list 사용 -Python3 성공
from collections import deque
import sys
input = sys.stdin.readline
M, N, H = map(int, input().split())
boxes = []
queue = deque([])
in_count = 0
not_in_count = 0
days = 0
for h in range(H):
    floor = []
    for x in range(N):
        row = list(map(int, input().rstrip().split()))
        for y in range(M):
            if row[y] == 1:
                queue.append([x, y, h, 0])
            elif row[y] == -1:
                not_in_count += 1
        floor.append(row)
    boxes.append(floor)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0 ,0]
dh = [0, 0, 0, 0, -1, 1]
in_count = len(queue)

while queue:
    x, y, h, count = queue.popleft()
    days = count
    if boxes[h][x][y] != 1:
        continue
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nh = h + dh[i]
        if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M:
            if boxes[nh][nx][ny] == 0:
                boxes[nh][nx][ny] = 1
                queue.append((nx, ny, nh, count + 1))

counts = 0
for h in range(H):
    for x in range(N):
        for y in range(M):
            if boxes[h][x][y] == 1:
                counts += 1

if counts != (M * N * H - not_in_count):
    days = -1
print(days)

# # BFS - vistied Set 사용 - PyPy3 성공
# from collections import deque
# import sys
# input = sys.stdin.readline
# M, N, H = map(int, input().split())
# boxes = []
# queue = deque([])
# visited = set()
# not_in_count = 0
# days = 0
# for h in range(H):
#     floor = []
#     for x in range(N):
#         row = list(map(int, input().rstrip().split()))
#         for y in range(M):
#             if row[y] == 1:
#                 queue.append([x, y, h, 0])
#             elif row[y] == -1:
#                 not_in_count += 1
#         floor.append(row)
#     boxes.append(floor)

# dx = [-1, 1, 0, 0, 0, 0]
# dy = [0, 0, -1, 1, 0 ,0]
# dh = [0, 0, 0, 0, -1, 1]

# while queue:
#     x, y, h, count = queue.popleft()
#     if (x, y, h) not in visited:
#         visited.add((x, y, h)) 
#         if len(visited) == (M * N * H - not_in_count):
#             days = count
#             break
#         for i in range(6):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             nh = h + dh[i]
#             if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M:
#                 if boxes[nh][nx][ny] == 0:
#                     queue.append((nx, ny, nh, count + 1))
# if len(visited) != (M * N * H - not_in_count):
#     days = -1
# print(days)
