# https://www.acmicpc.net/problem/1987

# 세로 R, 가로 C 칸으로된 표 모양의 보드
# 보드의 각 칸에는 대문자 알파벳, 좌측 상단 칸에는 말이 놓여있다.
# 말은 상하좌우로 인접한 네 칸중의 한 칸으로 이동 가능
# 같은 앒벳이 적힌 칸을 두번 지날 수 없다.
# 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램 작성
# 백트래킹?
# import sys

# input = sys.stdin.readline

# N, C = map(int, input().rstrip().split())

# grid = []
# for _ in range(N):
#     grid.append(list(input().rstrip()))

# move_x = [1, -1, 0, 0]
# move_y = [0, 0, 1, -1]

# def is_valid_move(next_x, next_y):
#     return (next_x < N and next_y < C) and (next_x >= 0 and next_y >= 0)

# def dfs(stack, visited):
#     if len(stack) == 0:
#         return
#     x, y = stack.pop()
#     print(x, y, visited)
#     for dx, dy in zip(move_x, move_y):
#         next_x = x + dx
#         next_y = y + dy
#         if not is_valid_move(next_x, next_y):
#             continue
#         next_alpha = grid[next_x][next_y]
#         if next_alpha in visited:
#             continue
#         stack.append((next_x, next_y))
#         visited.append(next_alpha)
#         dfs(stack, visited)
#         stack.pop()
#         visited.pop()

# stack = [(0, 0)]
# visited = list()
# visited.append(grid[0][0])
# dfs(stack, visited)


### 구조적인 문제점 수정!

import sys

input = sys.stdin.readline
N, C = map(int, input().rstrip().split())
grid = []
for _ in range(N):
    grid.append(list(input().rstrip()))

move_x = [1, -1, 0, 0]
move_y = [0, 0, 1, -1]

def is_valid_move(next_x, next_y):
    return (next_x < N and next_y < C) and (next_x >= 0 and next_y >= 0)

result = 0
def dfs(x, y, visited):
    global result
    result = max(result, len(visited))
    if result == 26:
        return

    for dx, dy in zip(move_x, move_y):
        next_x = x + dx
        next_y = y + dy
        if not is_valid_move(next_x, next_y):
            continue
        next_alpha = grid[next_x][next_y]
        if next_alpha in visited:
            continue
        visited.add(next_alpha)
        dfs(next_x, next_y, visited)
        visited.remove(next_alpha)

visited = set()
visited.add(grid[0][0])
dfs(0, 0, visited)
print(result)

# .. 이것도 안된다. 7%에서 끊김
# 나갔다 와서 한번만 더 5분만 더 고민ㅎ보기

# 흠.. pypy로 하니깐 되네 열받누
