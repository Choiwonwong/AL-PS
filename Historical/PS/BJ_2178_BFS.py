from collections import deque # Queue를 위한 자료형 import

N, M = map(int, input().split())
maps = [] # 미로 값
for _ in range(N):
    maps.append(list(input()))

def checkin_map(i, j, n, m): # 좌표값이 벗어났는지 체크하는 함수
    return 0 <= i < n and 0 <= j < m

queue = deque() # 큐 선언
visited = set() # 방문 자료형 선언
counts = 0 # 결과값 초기화
queue.append((0, 0)) # 최초 위치 입력
while True: # 더 이상 방문할 위치가 없을 때 종료
    for _ in range(len(queue)):
        x, y = map(int, queue.popleft())
        if (x, y) not in visited: # 방문하지 않은 지점일 경우
            visited.add((int(x), int(y))) # 방문 리스트에 입력
            if checkin_map(x+1, y, N, M) and maps[x+1][y] == '1':
                queue.append((x+1,y))
            if checkin_map(x-1, y, N, M) and maps[x-1][y] == '1':
                queue.append((x-1,y))
            if checkin_map(x, y+1, N, M) and maps[x][y+1] == '1':
                queue.append((x,y+1))
            if checkin_map(x, y-1, N, M) and maps[x][y-1] == '1':
                queue.append((x,y-1))
    counts += 1 # Depth 증가
    if (N-1, M-1) in visited: # 만약, 목표 지점에 도달한다면 중지
        break 
print(counts)