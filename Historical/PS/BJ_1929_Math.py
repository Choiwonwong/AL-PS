# 에라토스테네스의 체 사용

M, N = map(int, input().split())
pns = set([i for i in range(max(2, M), N+1)]) # 1을 제외하기 위한 예외 처리

for i in range(2, N):
    cur = set([i for i in range(i + i, N+1, i)])
    pns -= cur
prime_arr = sorted(list(pns))
for n in prime_arr:
    print(n)