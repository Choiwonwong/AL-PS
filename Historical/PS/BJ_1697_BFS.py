# DP로 할뻔하다 BFS였다고 합니다.

from collections import deque
N, K = map(int, input().split())
MAX= max(N, K) * 2
if N >= K:
    print(N-K)
else:
    visited = set()
    queue = deque([(N, 0)])
    while queue:
        cur, time = queue.popleft()
        if cur == K:
            break
        if cur not in visited:
            visited.add(cur)
            if cur+1 <= K :
               queue.append((cur+1, time+1)) 
            if cur-1 >= 0:
                queue.append((cur-1, time+1)) 
            if 2 * cur < MAX:
                queue.append((2 * cur, time+1)) 
    print(time)