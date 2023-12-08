# 팩토리얼이 계산될 때 2와 5의 개수를 구하면 된다.
# 실제 팩토리얼 값 세는 것 불가능  N <= 500

N = int(input())
count = [0, 0]
for i in range(1, N+1):
    check2 = i
    while True:
        if check2 % 2 != 0:
            break
        else:
            count[0] += 1
        check2 //= 2
    check5 = i
    while True:
        if check5 % 5 != 0:
            break
        else:
            count[1] += 1
        check5 //= 5
print(min(count)) 