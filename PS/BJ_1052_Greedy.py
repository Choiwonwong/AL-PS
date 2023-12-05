# 만약, 물병을 추가해야한다면, 그때마다 이진수로 표현이 가능한지 체크

N, K = map(int, input().split())
answer = 0
while bin(N)[2:].count('1') > K: # 표현할 이진수의 개수가 가져가야할 물병 개수보다 많다면 물병 추가
    answer +=1
    N += 1
print(answer)