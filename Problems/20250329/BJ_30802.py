# 웰컴 키트

## 티셔츠 한 장과 펜 한 자루가 포함된 웰컴 키트
## 티셔츠는 S, M, L, XL, XXL, 그리고 XXXL의 6가지 사이즈가 있습니다. 티셔츠는 같은 사이즈의 T장 묶음으로만 주문 가능
## 펜은 한 종류로, P자루씩 묶음으로 주문하거나 한 자루씩 주문

N = int(input())
t_shirts = list(map(int, input().split()))
T, P = map(int, input().split())

result = 0
for t_shirt in t_shirts:
    count = t_shirt // T
    if t_shirt % T != 0:
        count += 1
    result += count

print(result)
print(f"{N // P} {N % P}")