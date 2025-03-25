# heap 사용
import sys
import heapq
input = sys.stdin.readline

N = int(input().rstrip())
opers = [int(input().rstrip()) for _ in range(N)]
max_heap = []

for oper in opers:
    if oper == 0:
        if max_heap:
            print(-heapq.heappop(max_heap))
        else:
            print(0)
    else:
        heapq.heappush(max_heap, -oper)