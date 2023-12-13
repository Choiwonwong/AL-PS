# heap 사용
import heapq, sys
T = int(input())
operations = [int(sys.stdin.readline().rstrip()) for _ in range(T)]
heap = []
for oper in operations:
    if oper == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, oper)