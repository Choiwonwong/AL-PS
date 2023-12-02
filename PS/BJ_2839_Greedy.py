N = int(input())
count = 0
while N > 0:
    if N % 5 == 0:
        count += N // 5
        break
    else:
        N -= 3
        count += 1
if N < 0:
    count = -1
print(count)

# 원래 5의 배수인지 확인
# 3으로 5의 배수를 만든다.
# 안되면 -1