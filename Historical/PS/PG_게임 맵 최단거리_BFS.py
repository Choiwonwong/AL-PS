from collections import deque # queue 자료형 import
            
def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0]) #크기 선언
    queue = deque()
    queue.append((0, 0)) # Queue 초기화
    dx= [-1, 1, 0, 0] 
    dy= [0, 0, -1, 1]
    
    while queue: # BFS 로직
        x, y = queue.popleft() # 현재 위치 Pop
        for i in range(4): # 4 방향으로 진행
            nx, ny = x + dx[i], y + dy[i] # 다음 위치
            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 
                continue
            if maps[nx][ny] == 0: # 못 갈 때
                continue
            if maps[nx][ny] == 1: # 갈 수 있을 때
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))  
    
    if maps[n-1][m-1] > 1:
        answer = maps[n-1][m-1] # 도착했을 때의 위치
    return answer