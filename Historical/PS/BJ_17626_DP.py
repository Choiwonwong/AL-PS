# Brute Force를 응용하면 Python3에서도 해결 가능
n = int(input())
arr = [0 if i**0.5%1 else 1 for i in range(n+1)] # 제곱수는 1로 저장

min_ = 4
for i in range(int(n**0.5), 0, -1):
    if arr[n] : # n이 제곱수일 경우
        min_=1
        break
    elif arr[n-i**2] : # 나머지가 제곱수일 경우
        min_=2
        break
    else:
        for j in range(int((n-i**2)**0.5), 0, -1):
            if arr[(n-i**2)-j**2]: # 제곱수를 한번 더 뺀 나머지가 제곱수일 경우
                min_=3
print(min_)

## DP 풀이
## 아래의 두 풀이는 PyPy3 인터프리터에서는 성공 - Python3에서는 시간 초과 발생 -> 다른 방법 찾아봄
# import sys
# input = sys.stdin.readline

# N = int(input())
# dp = [0] * (N+1)
# dp[1] = 1
# for i in range(2, N+1):
#     dp[i] = min([dp[i-j ** 2] + 1 if i != j ** 2 else 1 for j in range(1, int(i ** 0.5) + 1)])
# print(dp[N])

# import sys
# input = sys.stdin.readline

# N = int(input())
# dp = [0] * (N+1)
# dp[1] = 1
# for i in range(2, N+1):
#     cur_list = []
#     for j in range(1, int(i ** 0.5) + 1):
#         if i == j ** 2:
#             cur_list.append(1)
#         else:
#             cur_list.append(dp[i-j ** 2] + 1)
#     dp[i] = min([dp[i-j ** 2] + 1 if i != j ** 2 else 1 for j in range(1, int(i ** 0.5) + 1)])
# print(dp[N])