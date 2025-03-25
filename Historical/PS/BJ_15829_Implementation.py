N = int(input())
S = input()
codes = []
for s in S: # 문자열 아스키 코드 변환
    codes.append(ord(s) - ord('a')+1)
answer = 0
for i in range(len(codes)): # 구현
    answer += codes[i] * (31 ** i)
print(answer % 1234567891)