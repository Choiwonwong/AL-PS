import sys
input = sys.stdin.readline
N, M = map(int, input().split()) # N, M 입력
known_fact = list(map(int, input().split()))
known_facts = [] # 시작점
for i in range(known_fact[0]):
    known_facts.append(known_fact[i+1])

parties = []
for _ in range(M):
    party = list(map(int, input().split()))
    parties.append(party[1:])

graph = [[] for _ in range(N+1)] # 그래프 모델링

for i in range(M): # 사람의 번호별 속한 파티의 인덱스를 모델링
    for j in parties[i]:
        graph[j].append(i)

visited = set() # 방문한 -> 알고 있는 사람들 집합
while known_facts:
    cur = known_facts.pop()
    if cur not in visited:
        visited.add(cur)
        for i in graph[cur]:
            known_facts.extend(parties[i])

counts = 0
for party in parties:
    flag = False
    for known_fact in visited:
        if known_fact in party:
            flag = True
            break
    if flag:
        counts += 1

print(M - counts)
# 반례    
# 8 4
# 1 1
# 3 1 2 3
# 3 4 5 6
# 3 6 7 8
# 2 3 8