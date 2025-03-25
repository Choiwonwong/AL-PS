# 피보나치 수열
N = int(input())
if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    count = 2
    n1 = 2
    n2 = 1
    for i in range(2, N):
        n = n1 + n2
        n2 = n1
        n1 = n
    print(n % 10007)