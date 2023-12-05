# DP 사용
N = int(input())
tri = []
for _ in range(N):
    tri.append(list(map(int, input().split())))
for i in range(1, N):
    tri[i][0] = tri[i-1][0] + tri[i][0]
    for j in range(1, i):
        tri[i][j] = tri[i][j] + max(tri[i-1][j-1], tri[i-1][j])
    tri[i][i] = tri[i-1][i-1] + tri[i][i]
print(max(tri[N-1]))