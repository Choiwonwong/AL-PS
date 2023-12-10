# Dense Rank 정하기
N = int(input())
arrs = [list(map(int, input().split())) for _ in range(N)]
scores = []
for i in range(N):
    rank = 1
    for j in range(N):
        weight_flag = False
        height_flag = False
        if j == i:
            continue
        if arrs[i][0] < arrs[j][0]:
            weight_flag = True
        if arrs[i][1] < arrs[j][1]:
            height_flag = True
        if weight_flag and height_flag:
            rank += 1
    scores.append(str(rank))
print(" ".join(scores))