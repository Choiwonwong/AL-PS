# Divide & Conquer + Recursion
import sys
input = sys.stdin.readline

def check_papaer(N, papers, w_count, b_count):
    if N <= 1:
        return 0
    N_2 = N // 2
    xs = [(0, N_2), (0, N_2), (N_2, N), (N_2, N)]
    ys = [(0, N_2), (N_2, N), (0, N_2), (N_2, N)]

    check = 0
    for i in range(N):
        for j in range(N):
            if papers[i][j] == 1:
                check += 1
    if check == N * N:
        return w_count, b_count + 1
    elif check == 0:
        return w_count +1, b_count

    for idx in range(4):
        check = 0
        sub_paper = []
        for i in range(xs[idx][0], xs[idx][1]):
            row = []
            for j in range(ys[idx][0], ys[idx][1]):
                if papers[i][j] == 1:
                    check += 1
                row.append(papers[i][j])
            sub_paper.append(row)
        if check == N_2 * N_2:
            b_count += 1
        elif check == 0:
            w_count += 1
        else:
            w_count, b_count = check_papaer(N_2, sub_paper, w_count, b_count)
    return w_count, b_count

N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]
for i in check_papaer(N, papers, 0, 0):
    print(i)