idx = 1
while True:
    L, P, V = map(int, input().split())
    if [L, P, V] == [0, 0, 0]:
        break
    result = (V // P) * L +  min(V % P, L) # 나눈 횟수만큼은 L번 가능, 남은 구간은 따로 min 처리
    print(f"Case {idx}: {result}")
    idx += 1