import sys
N = int(input())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
matrix.sort(key=lambda x: [x[0], x[1]])
for x, y in matrix:
    print(x, y)