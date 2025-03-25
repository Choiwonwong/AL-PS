# 안정적인 문자열을 만들기 위한 최소 연산의 수

# 1. 빈 문자열 안정적
# 2. S가 안정적이라면, {S} 도 안정적
# 3. S와 T가 안정적이라면, ST도 안정적

# 연산은 여는 -> 닫는 or 닫는 -> 여는 뿐이다.
# Stack을 활용한 Greedy 적용 가능

T = 1
while True:
    S = input()
    if '-' in S:
        break
    answer = 0
    stack = [] # 남아 있는 불안정한 문자열을 담음
    for s in S: # 
        if s == "}" and stack:
            if stack[-1] == "{":
                stack.pop()
                continue
        stack.append(s)

    for i in range(0, len(stack), 2): # 두 개씩 짝을 지어 변경해야할 횟수 계산
        if stack[i] != "{":
            answer += 1
        if stack[i+1] != "}":
            answer += 1
    print(f"{T}. {answer}")
    T += 1