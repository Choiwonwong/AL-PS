# Dictionary로 숫자 개수 담기
N = int(input())
arr_n = list(map(int, input().split()))

M = int(input())
arr_m = list(map(int, input().split()))

maps = {}

for n in arr_n:
    if n not in maps:
        maps[n] = 1
    else:
        maps[n] += 1

counts = []
for m in arr_m:
    if m in maps:
        counts.append(maps[m])
    else:
        counts.append(0)

for i in counts:
    print(i, end=" ")