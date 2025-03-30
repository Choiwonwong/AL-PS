N, M = map(int, input().split())

matrix_a = []
matrix_b = []
result = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    row = list(map(int, input().split()))
    matrix_a.append(row)

for i in range(N):
    row = list(map(int, input().split()))
    matrix_b.append(row)

for i in range(N):
    for j in range(M):
        print(matrix_a[i][j] + matrix_b[i][j], end = " ")
    print()