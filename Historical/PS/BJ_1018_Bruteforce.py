M, N = map(int, input().split())

boards = [list(input()) for _ in range(M)]

# 하얀색 시작
white_board = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
]

counts = []
for i in range(M-7):
    for j in range(N-7):
        count = 0
        for k in range(8):
            for l in range(8):
                if white_board[k][l] != boards[i+k][j+l]:
                    count += 1
        counts.append(count)

# 검은색 시작
black_board = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
]

count_black = []
for i in range(M-7):
    for j in range(N-7):
        count = 0
        for k in range(8):
            for l in range(8):
                if black_board[k][l] != boards[i+k][j+l]:
                    count += 1
        counts.append(count)

print(min(counts))