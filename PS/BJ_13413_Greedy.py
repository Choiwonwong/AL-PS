# 1. 배치된 말 중 임의의 2개의 말을 골라 위치 바꾸기
# 2. 말 1개를 놓아 색상 변경

# 이건 무조건 1.을 많이 수행하는 것이 최선이다.
T = int(input())
for _ in range(T):
    N = int(input())
    start = input()
    target = input()
    diff = [0, 0] # White로 바꿔야하는 경우, Black로 바꿔야하는 경우
    for i in range(len(start)):
        if start[i] != target[i]:
            if start[i] == "B":
                diff[0] += 1
            else:
                diff[1] += 1
    print(max(diff)) # 두 변경 사항 중 최대값을 선택하면 된다.