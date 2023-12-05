T = int(input())
for _ in range(T):
    N, S = input().split()
    answer = ""
    for s in S:
        answer += s * int(N)
    print(answer)