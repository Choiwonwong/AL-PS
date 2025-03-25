# 수학 구현
# 정상을 찍기 전날만 필요함 - 이를 수식으로 계산 가능
A, B, V = map(int, input().split())
days = 1
if (V-A) % (A-B) == 0:
    days += (V-A) // (A-B)
else:
    days += ((V-A) // (A-B) + 1)
print(days)