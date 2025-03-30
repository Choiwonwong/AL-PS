# 과일 탕후루 - https://www.acmicpc.net/problem/30804
## 탕후루 앞뒤에서 a, b 개씩 빼서 2종류 이하만 남게 만들어야함.
## 만들 수 있는 탕후루 중에서 가장 길 때의 길이 반환

## 투포인터 or Greedy? 어캐 풀어야할까
## Greedy나 DP가 되려면 정렬을 할 수 있어야하는데, 이건 그게 안되기 때문에 적용 불가능
## 투 포인터로 접근하려면,, 
## N은 20만의 제약이 있음, 다행이 과일의 종류는 9개.
## set으로 잡아도 연산량이 클것으로 예상되긴함. in 절로 해도 N의 복잡도인거고,
## 이걸 앞에서부터 & 뒤에서부터 접근하면 N의 복잡도가 들어감. 따라서 하기 힘든 결정임.
## BFS, DFS를 써도 복잡도 상 안될 것으로 보임.
## 일단 과일 종류 몇개인지 판단하는 함수는 필요할 듯

# def check_under_two(tangs):
#     return len(set(tangs)) <= 2

# global results
# results = set()
# def dfs(tangs):
#     if check_under_two(tangs):
#         results.add(len(tangs))
#         return 
#     else:
#         dfs(tangs[1:])
#         dfs(tangs[:-1])

# N = int(input())
# tangs = list(input().split())
# dfs(tangs)
# print(max(results))

## 앞에서도 빼봐야하고 뒤에서도 빼봐야하는 상황 -> DFS처럼 접근하면 안되나?
## 결국 앞에서 하나 빼고, 뒤에서 하나 빼고 하면서 탕후루 길이를 줄여가고, 그 중에 처음으로 2를 닿으면 끝내면 되는거 아닌가?
## 근데 재귀로 풀면 복잡도 터지긴 할 듯
## 완전 탐색은 못하는디, 아무튼 문제에서 바라는 건, 최대 길이이기 때문에 유일한 답을 찾아야함.
## 중앙에서 탐색될 경우면 오케이긴한데, 만약 앞에서 쭉가는게 제일 좋으면 어캄? -> 백트래킹이 필요한건가?
## Recursion Depth 초과 발생

## 투 포인터 접근 진행
## 이게 앞과 뒤에서 오는게 아니라, 둘다 앞에서 시작해야함.
## 로직이 이런거지, 우선 right를 늘렸을 때 길이가 늘면 계속 +1
## right을 늘렸는데, 3을 초과하면 left를 계속 줄이기
from collections import defaultdict

N = int(input())
tangs = list(input().split())

def max_tangs_length(tangs):
    fruit_count = defaultdict(int)  # 각 과일 개수 저장
    left = 0
    max_length = 0

    for right in range(len(tangs)):
        fruit_count[tangs[right]] += 1
        
        # 과일 종류가 3개 이상이면 left 이동
        while len(fruit_count) > 2:
            fruit_count[tangs[left]] -= 1
            if fruit_count[tangs[left]] == 0:
                del fruit_count[tangs[left]]
            left += 1  # left를 이동하여 범위를 줄이기
        
        # 최대 길이 갱신
        max_length = max(max_length, right - left + 1)
    
    return max_length
print(max_tangs_length(tangs))