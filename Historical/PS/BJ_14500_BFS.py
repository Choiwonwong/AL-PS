from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(M):
        queue = deque()
        queue.append((i, j, grid[i][j], 1, ""))
        if i < N-1 and j < M-1:
            queue.append((i, j, grid[i][j] + grid[i+1][j] + grid[i][j+1] +grid[i+1][j+1], 4, ""))
        while queue:
            x, y, value, depth, direction = queue.popleft()
            if depth == 4:
                if value > result:
                    result = value
            else:
                if x+1 < N:
                    queue.append((x+1, y, value + grid[x+1][y], depth +1, "D"))
                if y+1 < M and direction != "L":
                    queue.append((x, y+1, value + grid[x][y+1], depth +1, "R"))
                if 0 <= y-1 and direction != "R":
                    queue.append((x, y-1, value + grid[x][y-1], depth +1, "L"))        
                if depth == 2:
                    if direction == "D":
                        if x+1 < N:
                            if y + 1 < M:                    
                                queue.append((x+1, y+1, value + grid[x+1][y] + grid[x][y+1], 4, ""))
                            if 0 <= y - 1:
                                queue.append((x+1, y-1, value + grid[x+1][y] + grid[x][y-1], 4, ""))
                    if direction == "R":
                        if y+1 < M:
                            if x + 1 < N:                    
                                queue.append((x+1, y+1, value + grid[x][y+1] + grid[x+1][y], 4, ""))
                            if 0 <= x - 1:
                                queue.append((x-1, y+1, value + grid[x][y+1] + grid[x-1][y], 4, ""))
                    if direction == "L":
                        if y-1 >= 0:
                            if x + 1 < N:                    
                                queue.append((x+1, y-1, value + grid[x][y-1] + grid[x+1][y], 4, ""))
                            if 0 <= x - 1:
                                queue.append((x-1, y-1, value + grid[x][y-1] + grid[x-1][y], 4, direction +  "LLUU"))
print(result)