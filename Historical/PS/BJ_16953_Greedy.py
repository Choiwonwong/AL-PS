A, B = map(int, input().split())
count = 1
while True:
    if A == B: # 찾을 수 있을 때
        break
    if B < 1: # 못찾을 때
        count = -1
        break
    if B % 10 == 1: # 일의 자리가 1이면 1을 떼기
        B //= 10
    elif B % 2 == 0: # 일의 자리가 2여야만 나누기
        B //= 2
    else: # 일의 자리가 둘 다 아니면 못만든다.
        count = -1
        break
    count += 1
print(count)