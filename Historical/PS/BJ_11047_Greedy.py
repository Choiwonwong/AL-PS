# N 개의 종류의 동전으로 K을 만들 때 필요한 동전 개수의 최솟값
# 값이 큰 동전부터 나누어지는지를 체크하고, 나누어질 때 거슬러주면 된다. -> Greedy
# 동전의 종류가 배수일 경우에 이 부분이 동적하긴 하는데, 일단 이를 보장해준다고 가정 
N, Target = map(int, input().split())
coins = []
counts = 0
for _ in range(N):
    coins.append(int(input())) # 동건 종류가 오름차순임이 보장
for i in reversed(range(N)):
    flag = Target // coins[i] # 현재 동전으로 거슬러 줄 수 있는지 판단
    if flag > 0:
        counts += flag # 거슬러주고
        Target -= flag * coins[i] # 빼기
print(counts)