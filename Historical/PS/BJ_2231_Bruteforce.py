# Brute Force로 1부터 검사
N = int(input())
M = 0
for i in range(1, N):
    tmp = i
    for j in str(i):
        tmp += int(j)
    if tmp == N:
        M = i
        break
print(M)
