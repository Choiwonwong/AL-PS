# Queue 사용

from collections import deque
N = int(input())
arr = [i for i in range(1, N+1)]
queue = deque(arr)

for i in range(N-1):
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])