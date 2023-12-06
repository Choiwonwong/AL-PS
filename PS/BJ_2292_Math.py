# 도착지부터 1로의 Depth를 구하기
# 한 층은 6의 배수로 원소들을 가짐
N = int(input())
count = 1
idx = 1
while N > 1:
    N -= 6 * idx
    count += 1
    idx += 1
print(count)