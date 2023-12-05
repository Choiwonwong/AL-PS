S = 1
for _ in range(3):
    S *= int(input())
S = list(str(S))
for i in range(10):
    print(S.count(str(i)))