# N과 M(4)
# https://www.acmicpc.net/problem/15652
## 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
## 1부터 N까지 자연수 중에서 M개를 고른 수열
## 같은 수를 여러 번 골라도 된다.
## 고른 수열은 비내림차순이어야 한다.
## 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

# def get_movable_idx(array, N, M):
#     for i in range(M-1, -1, -1):
#         if array[i] < N:
#             return i
        
# def increase_array(array, movable_idx, M):
#     array[movable_idx] += 1
#     base_line = array[movable_idx]
#     for idx in range(movable_idx, M):
#         if array[idx] > base_line:
#             array[idx] = base_line
#     return array

# def print_array(array):
#     for i in array:
#         print(i, end=" ")
#     print()

# N, M = map(int, input().split())

# current_step = [1 for _ in range(M)]
# end = [N for _ in range(M)]
# answer = [current_step]
# print_array(current_step)
# while current_step != end:
#     movable_idx = get_movable_idx(current_step, N, M)
#     current_step = increase_array(current_step, movable_idx, M)
#     print_array(current_step)

# 맞았의
## 이제 최적화 진행

def get_movable_idx(array, N, M):
    for i in reversed(range(M)):
        if array[i] < N:
            return i
        
def increase_array(array, movable_idx, M):
    array[movable_idx] += 1
    base_line = array[movable_idx]
    for idx in range(movable_idx, M):
        if array[idx] > base_line:
            array[idx] = base_line
    return array


N, M = map(int, input().split())

current_step = [1] * M
end = [N] * M 
answer = [current_step]
print(*current_step)
while current_step != end:
    movable_idx = get_movable_idx(current_step, N, M)
    current_step = increase_array(current_step, movable_idx, M)
    print(*current_step)
