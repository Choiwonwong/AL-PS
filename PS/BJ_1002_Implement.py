T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    answer = 0
    x_dist_sq, y_dist_sq = (x1-x2) ** 2, (y1-y2) ** 2
    if x_dist_sq + y_dist_sq == 0: # 두 원의 중심이 같을 때
        if r1 == r2: # 반지름까지 같다면, 교점은 무한대
            answer = -1
        else: # 다르면 0
            answer = 0
    else:
        dist = (x_dist_sq + y_dist_sq) ** 0.5
        if (dist == r1+r2) or (dist == abs(r1 - r2)): # 두 원이 한 점에서 만날 때
            answer = 1
        elif (dist < abs(r1 - r2)) or (dist > r1+r2): # 두 원이 접하지 않을 때
            answer = 0
        else: # 두 원이 두 점에서 만날 때
            answer = 2
    print(answer)