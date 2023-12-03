N = int(input())
buttons = [300, 60, 10]
counts = []
for button in buttons: # 버튼마다 계산
    tmp = N // button
    counts.append(tmp)
    N = N % button
if N != 0: # 표현이 안될 경우
    print("-1")
else: # 표현될 경우
    for count in counts:
        print(count , end=" ")