# Queue
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    opers = input().rstrip()
    N = int(input())
    array = deque(input().rstrip()[1:-1].split(',')) # 배열 입력 처리
    forward = True # 순방향, 역방향 처리 플래그
    error = False # 에러 발생 시 플래그
    if N == 0: # 원소가 없을 경우 예외 처리
        array = []
    for oper in opers: # 연산 시작
        if oper == 'R': # 방향 전환
            forward = False if forward else True
        else:
            if array:
                if forward: # 순방향
                    array.popleft() # 앞 원소를 뺌
                else: # 역방향
                    array.pop() # 뒤 원소를 뺌
            else:
                error = True # 에러 처리
                break
    if not error:
        if forward:
            print("[" + ",".join(array) + "]")
        else:
            print("[" + ",".join(reversed(array)) + "]")
    else:
        print("error")

# R이 나올때 마다 
# from collections import deque
# import sys
# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     opers = input().rstrip()
#     N = int(input())
#     array = deque(input().rstrip()[1:-1].split(','))
#     answer = ""
#     if N == 0:
#         array = []
#     for oper in opers:
#         if oper == 'R':
#             array.reverse()
#         else:
#             if array:
#                 array.popleft()
#             else:
#                 answer = "error"
#                 break
#     if answer == "":
#         print("[" + ",".join(array) + "]")
#     else:
#         print(answer)