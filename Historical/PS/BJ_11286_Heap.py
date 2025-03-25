# heap 사용
# 정수 트릭을 사용하면 됨.
# 0은 -> 0
# 1의 경우 -> 1.2로 저장
# -1의 경우 -> 1.1로 저장
# 2의 경우 2.2로 저장
# -2의 경우 2.1로 저장

import sys
import heapq
input = sys.stdin.readline

N = int(input().rstrip())
opers = [int(input().rstrip()) for _ in range(N)]
abs_heap = []

for oper in opers:
    if oper == 0:
        if abs_heap:
            cur = heapq.heappop(abs_heap)
            if (cur * 10 % 10) == 1:
                cur = -(cur * 10 // 10)
            else:
                cur = cur * 10 // 10
            print(int(cur))
        else:
            print(0)
    else:
        cur = abs(oper)
        if oper > 0:
            cur += 0.2
        else:
            cur += 0.1
        heapq.heappush(abs_heap, cur)