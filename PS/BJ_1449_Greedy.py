# 왼쪽에서 떨어진 거리만큼 물이 센다
# 길이가 L인 테이프를 무제한
# 좌우 0.5만큼은 붙여야함.
# 필요한 테이프의 최소 개수

# 1. 기준점을 골라야함.
# 2. 다음 기준점에 포함이 되는지 판단해야함.
N, L = map(int, input().split())
leak_spots = list(map(int, input().split()))
leak_spots.sort()
count = 1
idx = 1
stand = leak_spots[0]
while idx < N: # N을 다 순회함
    if leak_spots[idx] - stand < L: # 만약, 기준점과 현재 인덱스의 차이가 L보다 작으면 -> 같이 붙임
        pass
    else: # 아니면, 새로운 테이프를 붙여야함.
        count += 1
        stand = leak_spots[idx]
    idx+=1
print(count)