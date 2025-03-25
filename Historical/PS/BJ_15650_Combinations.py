# from itertools import combinations
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())

# for combi in combinations(range(1, N+1), M):
#     print(str(combi).replace(",", "").replace("(", "").replace(")", ""))

# 라이브러리 없이 조합 구현
def combinations(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [str(array[i])]
        else:
            for next in combinations(array[i+1:], r-1):
                yield [str(array[i])] + next

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

for combi in combinations(range(1,N + 1), M):
    print(" ".join(combi))