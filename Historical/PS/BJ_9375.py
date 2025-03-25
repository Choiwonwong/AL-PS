# 계단은 한 번에 하나 or 두 칸
# 연속된 세 개의 계단은 밟으면 안됨
# 마지막 도착 계단은 필수
import sys
T = int(input())
for _ in range(T):
    N = int(input())
    setting = {}
    for _ in range(N):
        name, cate = sys.stdin.readline().rstrip().split()
        if cate not in setting:
            setting[cate] = 1
        else:
            setting[cate] += 1
    result = 1
    for count in setting.values():
        result *= (count + 1)
    print(result -1)