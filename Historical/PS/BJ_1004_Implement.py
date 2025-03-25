# 출발지와 도착지가 몇개의 행성계에 속했는지를 판단
# 행성계들이 맞닿거나 교차하는 경우는 없다. 또한 출발지와 도착점이 경계에 있는 경우는 없다.

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    count= 0
    N = int(input())
    for _ in range(N):
        cx, cy, r = map(int, input().split())
        check_star = ((x1 - cx) ** 2 + (y1 - cy) ** 2) < (r * r)
        check_dest = ((x2 - cx) ** 2 + (y2 - cy) ** 2) < (r * r)
        if check_star: # 도착지에 속한 행성계일 경우
            count += 1
        if check_dest: # 도착지에 속한 행성계일 경우
            count += 1
        if check_star and check_dest: # 출발지와 도착점이 같은 행성계에 속했을 때
            count -= 2
    print(count)