# # 수학 공식..
N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
permu = []
count = 1
index = 0
while arr:
    index = (index + K - 1) % len(arr)
    permu.append(str(arr.pop(index)))

answer = ", ".join(permu)
print("<" + answer + ">")

# Queue 자료형을 이용
from collections import deque
N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
permu = []
queue = deque(arr)
while queue:
    queue.rotate(-K + 1)
    permu.append(str(queue.popleft()))
answer = ", ".join(permu)
print("<" + answer + ">")