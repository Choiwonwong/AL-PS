# N과 M (5)
# https://www.acmicpc.net/problem/15654

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

from itertools import permutations

for permutation in permutations(arr, M):
    print(*permutation)

### 원래라면
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

used = [False] * N  # 방문 체크 배열
result = []  # 현재 선택한 순열을 저장

def backtrack():
    if len(result) == M:
        print(*result)
        return
    
    for i in range(N):
        if not used[i]:  # 아직 사용하지 않은 숫자라면
            used[i] = True  # 방문 표시
            result.append(arr[i])  # 숫자 추가
            backtrack()  # 다음 숫자 선택을 위한 재귀 호출
            result.pop()  # 원상 복구
            used[i] = False  # 방문 해제

backtrack()
