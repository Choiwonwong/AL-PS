N = int(input())
meetings = []

for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 종료 시간을 기준으로 정렬
meetings.sort(key=lambda x: (x[1],x[0]))

# 초기값 선택
end_time = meetings[0][1]
count = 1
# 초기값 이후 가장 빨리 끝나는 것을 선택
for i in range(1, N):
    if meetings[i][0] >= end_time:
        end_time = meetings[i][1]
        count += 1
print(count)