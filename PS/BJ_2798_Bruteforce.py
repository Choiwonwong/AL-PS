# # Simple Brute force
N, M = map(int, input().split())
cards = list(map(int, input().split()))
case = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sums = cards[i]+cards[j]+cards[k]
            if sums <= M:
                case.append(sums)
print(max(case))

# BF with Combinations
from itertools import combinations
N, M = map(int, input().split())
case = []
cards = list(map(int, input().split()))
for i, j, k in combinations(cards, 3):
    sums = i +j + k
    if sums <= M:
        case.append(sums)
print(max(case))