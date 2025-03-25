# Sort
import sys
N = int(sys.stdin.readline().lstrip())
grids = [list(map(int, sys.stdin.readline().lstrip().split())) for _ in range(N)]
grids.sort(key=lambda x: [x[1],x[0]])
for grid in grids:
    print(grid[0], grid[1])