# BFS 사용
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    start, target = map(int, input().split())
    queue = deque()
    queue.append((start, ""))
    visited = [False] * 10000
    visited[start] = True
    while queue:
        n, opers = queue.popleft()
        if n == target:
            print(opers)
            break
        
        next_d = (2 * n) % 10000
        next_s = n -1 if n > 0 else 9999
        next_l = (n // 1000 + (n % 1000)*10)
        next_r = (n // 10) + (n % 10)*1000

        if not visited[next_d]:
            visited[next_d] = True
            queue.append((next_d, opers + "D"))
        if not visited[next_s]:
            visited[next_s] = True
            queue.append((next_s, opers + "S"))
        if not visited[next_l]:
            visited[next_l] = True
            queue.append((next_l, opers + "L"))
        if not visited[next_r]:
            visited[next_r] = True
            queue.append((next_r, opers + "R"))

# # BFS 사용 -> 최적화가 될 된 코드
# from collections import deque
# import sys
# input = sys.stdin.readline

# def transform(A):
#     d1 = A // 1000
#     d2 = (A % 1000) // 100
#     d3 = (A % 100) // 10
#     d4 = A % 10
#     return d1, d2, d3, d4

# def oper_d(d1, d2, d3, d4):
#     n = ((d1 * 10 + d2) * 10 + d3) * 10 + d4
#     return transform((2 * n) % 10000)

# def oper_s(d1, d2, d3, d4):
#     n = ((d1 * 10 + d2) * 10 + d3) * 10 + d4
#     result = n -1 if n > 0 else 9999
#     return transform(result)

# def oper_l(d1, d2, d3, d4):
#     return d2, d3, d4, d1

# def oper_r(d1, d2, d3, d4):
#     return d4, d1, d2, d3

# T = int(input())
# for _ in range(T):
#     start, target = map(int, input().split())
#     d1, d2, d3, d4 = transform(start)
#     queue = deque([(d1, d2, d3, d4, "")])
#     # visited = set()
#     while queue:
#         d1, d2, d3, d4, opers = queue.popleft()
#         # visited.add((d1, d2, d3, d4))
#         if (((d1 * 10 + d2) * 10 + d3) * 10 + d4) == target:
#             print(opers)
#             break
        
#         next_d = list(oper_d(d1, d2, d3, d4))
#         next_s = list(oper_s(d1, d2, d3, d4))
#         next_l = list(oper_l(d1, d2, d3, d4))
#         next_r = list(oper_r(d1, d2, d3, d4))

#         # if tuple(next_d) not in visited:
#         next_d.append(opers + "D")
#         queue.append(next_d)
#         # if tuple(next_s) not in visited:
#         next_s.append(opers + "S")
#         queue.append(next_s)
#         # if tuple(next_l) not in visited:
#         next_l.append(opers + "L")
#         queue.append(next_l)
#         # if tuple(next_r) not in visited:
#         next_r.append(opers + "R")
#         queue.append(next_r)