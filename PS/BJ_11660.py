import sys
input = sys.stdin.readline

# N, M = map(int, input().split())
# cum_grids = []
# for i in range(N):
#     tmp = 0
#     tmp_list = []
#     for j in list(map(int, input().split())):
#         tmp += j
#         tmp_list.append(tmp)
#     cum_grids.append(tmp_list)
        
# for _ in range(M):
#     cum_sum = 0
#     x1, y1, x2, y2 = map(int, input().split())
#     for x in range(x1-1, x2):
#         if y1 == y2:
#             if y1 == 1:
#                 cum_sum += cum_grids[x][0]
#             else:
#                 cum_sum += (cum_grids[x][y2-1] - cum_grids[x][y1-2])
#         else:
#             if y1 == 1:
#                 cum_sum += cum_grids[x][y2-1]
#             else:
#                 cum_sum += (cum_grids[x][y2-1] - cum_grids[x][y1-1])
#     print(cum_sum)

# 부분합을 제대로 사용
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

prefix_sum = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        prefix_sum[i][j] = arr[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

print(prefix_sum)
def calculate_subarray_sum(x1, y1, x2, y2):
    return prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = calculate_subarray_sum(x1, y1, x2, y2)
    print(result)