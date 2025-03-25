N = int(input())
roads = list(map(int, input().split()))
oils = list(map(int, input().split()))

stops = [0] # 주유할 주유소의 인덱스를 담을 리스트
for i in range(1, N-1):
    if oils[stops[-1]] > oils[i]: # 만약, 현재 위치보다 가격이 싼 장소가 나올 때만 추가
        stops.append(i)

costs = 0
min_stop = oils.index(min(oils[:-1])) # 가장 싼 위치 인덱스

for idx in range(len(stops)): # 주유할 장소만큼만 반복하면 됨
    if stops[idx] == min_stop: # 만약 최저 가격이라면
        costs += sum(roads[stops[idx]:]) * oils[stops[idx]] # 끝
        break
    costs += sum(roads[stops[idx]:stops[idx+1]]) * oils[stops[idx]] # 아니라면 다음 주유소까지 주유

print(costs)