T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    floor = 1
    room = 1
    for i in range(1, N):
        if i % H == 0:
            room += 1
            floor = 1
        else:
            floor +=1
    answer = floor * 100 + room
    print(answer)