# Brute Force
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())    
if M > 0:
    not_buttons = list(map(int, input().split()))
    if M == 10: # 모든 버튼이 망가졌을 경우 예외 처리
        print(abs(N - 100))
        exit(0)
else: # 버튼이 하나도 안망가졌을 경우 예외 처리
    if len(str(N)) > abs(N - 100): # +, -로 가는게 빠를 경우
        print(abs(N - 100))    
    else: # 버튼을 누르는게 빠를 경우
        print(len(str(N)))
    exit(0)

channels = set(range(1000001)) # 전체 채널 선언
for not_button in not_buttons: # 고장난 버튼들을 순회
    tmp = set() # 바로 못가는 채널을 담을 Set 자료형 생성
    for channel in channels: # 모든 채널 순회
        if str(not_button) in str(channel): 
            tmp.add(channel) # 고장난 버튼이 포함된 채널을 담음
    channels -= tmp # 고장난 버튼이 포함된 채널 제외
channels = list(channels) # 남아있는 채널 리스트로 변환
lists = [abs(i - N) for i in channels] # 최솟값 계산
min_index = lists.index(min(lists)) # 최솟값 인덱스
count = len(str(channels[min_index])) + lists[min_index] # 개수 계산
if count > abs(N - 100): # 100에서 출발하는게 빠른 경우 판단
    print(abs(N - 100))
else:
    print(count)