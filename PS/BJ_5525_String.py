# 문자열 조작
import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
S = input().rstrip()

count = 0
idx = 1
pattern_count = 0
while idx < M -1:
    if S[idx-1] == 'I' and S[idx] == "O" and S[idx+1] == "I": # IOI 비교
        pattern_count += 1 # 패턴의 개수 증가
        if pattern_count == N: # 패턴이 N만큼 존재하면 
            count += 1 # 개수 + 1
            pattern_count -= 1 # 다음 패턴을 확인하기 위해 개수 - 1
        idx += 1 # O를 건너뛰기 위해 인덱스 하나 추가
    else:
        pattern_count = 0 # 패턴이 일치하지 않으면 0으로 초기화
    idx += 1
print(count)