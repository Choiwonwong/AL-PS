# 원래 팁 - (인덱스)의 팁을 받는다. 이 값들의 합이 최대가 되도록 배열 순서를 변경
# 음수면 팁을 안받음
# 따라서, 팁을 역정렬해서, 나온 값을 계산하면 됨. 어차피 안줄 놈을 맨 뒤로 보내자.

N = int(input())
tips = [int(input()) for _ in range(N)]
tips.sort(reverse=True)

answer = 0
for i in range(len(tips)):
    tip = tips[i] - i
    if tip > 0:
        answer += tip
print(answer)