import sys
input = sys.stdin.readline
N = int(input())
arr_x = list(map(int, input().split()))
unique_x = {}
for i, x in enumerate(sorted(list(set(arr_x)))):
    unique_x[x] = i
answer = []
for x in arr_x:
    answer.append(str(unique_x[x]))
print(" ".join(answer))