# 인접 리스트 사용하여 순서 보장

import sys
N = int(input())
arrs = [[] for _ in range(201)]
for i in range(N):
    age, name = sys.stdin.readline().split()
    arrs[int(age)].append(name)

for i in range(201):
    if arrs[i]:
        for j in range(len(arrs[i])):
            print(i, arrs[i][j])