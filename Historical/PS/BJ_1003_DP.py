# 피보나치 수열을 구할 때, 0과 1을 더하는 횟수를 구하라.
# DP 적용
T = int(input())
for _ in range(T):
    N = int(input())
    count0 = [0 for _ in range(max(2, N+1))] # 0의 개수 세기
    count1 = [0 for _ in range(max(2, N+1))] # 1의 개수 세기
    count0[0], count0[1] = 1, 0 # N - 0, 1 초기화
    count1[0], count1[1] = 0, 1 # N - 0, 1 초기화
    for i in range(2, N+1):
        count0[i] = count0[i-1] + count0[i-2]
        count1[i] = count1[i-1] + count1[i-2]
    print(count0[N], count1[N])