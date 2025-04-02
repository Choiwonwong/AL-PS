# N과 M (9)
# https://www.acmicpc.net/problem/15663

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

used = [False] * N
result = []
visited = set()
def backtracking():
    if len(result) == M:
        str_result = " ".join([str(i) for i in result])
        if str_result not in visited:
            visited.add(str_result)
            print(str_result)
        return
    
    for i in range(N):
        if used[i] == False:
            result.append(arr[i])
            used[i] = True
            backtracking()
            result.pop()
            used[i] = False

backtracking()

