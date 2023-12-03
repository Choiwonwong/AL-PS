S = int(input())
N = 1
while True:
    tmp = (N * (N + 1)) // 2 # D = 1 등차수열의 합
    if tmp > S: # 그 값을 벗어날 때
        break
    N+=1
print(N-1)