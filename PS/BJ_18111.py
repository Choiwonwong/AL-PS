# 땅 고르기 수행
# (0, 0) -> 높이를 일정하게 바꾸야함.
# 1. (i, j) 가장 위에 있는 블록을 제거하여 인벤토리에 넣음
# 2. 인벤토리에서 블록을 하나 꺼내서 가장 위에 있는 블록 위에 놓음

# 1번 작업은 2초
# 2번 작업은 1초
# 땅 고르기에 걸리는 최소 시간과 땅의 높이 출력
# 땅의 최대 높이 256, 시작 인벤토리에는 B개 존재

# Brute Force지만, PyPy3로 제출했을때만 성공한다.
# Python3 컴파일러에서는 시간 초과

import sys

N, M, B = map(int, input().split())
maps = [list(map(int, sys.stdin.readline().lstrip().split())) for _ in range(N)]
max_h = max(map(max, maps))
min_h = min(map(min, maps))

result = []
for h in range(min_h, max_h + 1):
    inventory = B
    time = 0
    flag = True
    upper = 0
    lower = 0
    for i in range(N):
        for j in range(M):
            diff = maps[i][j] - h
            if diff > 0:
                time += 2 * diff
                lower += diff
            elif diff < 0:
                time -= diff 
                upper -= diff
    if lower + inventory >= upper:
        result.append([time, h])
result.sort(key=lambda x: [x[0], -x[1]])
print(result[0][0], result[0][1])