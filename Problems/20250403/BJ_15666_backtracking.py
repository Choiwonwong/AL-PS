# N과 M (12)
# https://www.acmicpc.net/problem/15666

# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다. # 총 M번 
# 근데 결과는 같으면 안됨.
# 고른 수열은 비내림차순이어야 한다.

# import sys

# N, M = map(int, sys.stdin.readline().rstrip().split())
# values = list(map(int, sys.stdin.readline().rstrip().split()))
# values.sort()

# visited = [0] * N
# results = set()
# result = []
# def backtracking():
#     if len(result) == M:
#         str_result = " ".join([str(i) for i in sorted(result)])
#         if str_result not in results:
#             print(str_result)
#             results.add(str_result)
#         return
#     for i in range(N):
#         if visited[i] < M:
#             result.append(values[i])  
#             visited[i] += 1
#             backtracking()
#             result.pop()
#             visited[i] -= 1
        
# backtracking()
# 답은 나오는데 시간 복잡도가 터짐
# 최적화 해보기

## 단순 백트래킹으론 못푸는게 맞을 듯
## 또한 재귀로 접근하면 안될 것 같음.

# import sys

# N, M = map(int, sys.stdin.readline().rstrip().split())
# values = list(map(int, sys.stdin.readline().rstrip().split()))
# unique_values = set(values)
# sorted_unique_values = sorted(list(unique_values))

# result = []
# def tracking():
#     if len(result) == M:
#         print(*result)
#         return
#     current_value = result[-1] if len(result) > 0 else -1
#     current_value_index = sorted_unique_values.index(current_value) if current_value != -1 else 0
#     for next_value in sorted_unique_values[current_value_index:]:
#         result.append(next_value)
#         tracking()
#         result.pop()
            
# tracking()


import sys

N, M = map(int, sys.stdin.readline().split())
values = sorted(set(map(int, sys.stdin.readline().split())))  # 중복 제거 후 정렬

result = []
def backtrack(start):
    if len(result) == M:
        print(*result)
        return
    for i in range(start, len(values)):
        result.append(values[i])
        backtrack(i)
        result.pop()

backtrack(0)
