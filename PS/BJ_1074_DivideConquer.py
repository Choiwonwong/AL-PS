# 재귀 & 분할 정복 -> 시간 아웃
# import sys
# input = sys.stdin.readline

# def z_search(N, x, y, count):
#     if N > 1:
#         n_step = 2 ** (N-1)
#         n_count = 2 ** (2 * (N-1))
#         z_search(N-1, x, y, count)
#         z_search(N-1, x, y + n_step, count + n_count)
#         z_search(N-1, x + n_step, y, count + 2 *n_count)
#         z_search(N-1, x + n_step, y + n_step, count + 3 * n_count)
#     else:
#         maps[x][y] = count
#         maps[x][y+1] = count + 1
#         maps[x+1][y] = count + 2
#         maps[x+1][y+1] = count + 3

# N, r, c = map(int, input().split())
# maps = [[0 for _ in range(2**N)] for _ in range(2**N)]
# z_search(N, 0, 0, 0)
# print(maps[r][c])

## 분할 정복
# r, c가 위치하는 0 ~ 3 사분면을 찾고, count 값 갱신
# N = 1일 때 사분면의 값이 결과
def z_search(N, r, c):
    count = 0
    for n in range(N, 0, -1):
        n_step = 2 ** (n - 1)
        n_count = 2 ** (2 * (n - 1))
        quadrant = (r // n_step) * 2 + (c // n_step)
        count += n_count * quadrant
        r %= n_step
        c %= n_step
    return count

N, r, c = map(int, input().split())
result = z_search(N, r, c)
print(result)