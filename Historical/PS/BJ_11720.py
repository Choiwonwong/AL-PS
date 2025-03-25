N = int(input())
S = list(input())
answer = 0
for i in range(10):
    answer += i * S.count(str(i))
print(answer)