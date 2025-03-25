# + & - 0 ~ 9로만 이루어져 있음
# 결과값 최소가 되게 괄호를 치자.
# 마이너스가 나오면 그 뒤부터 다음 마이너스가 나오기 전까지 괄호를 치면 됨.
expression = input().split('-')
if len(expression) == 1: # - 가 없을 때
    result = sum(list(map(int, expression[0].split('+'))))
else:
    result = sum(list(map(int, expression[0].split('+')))) # - 이전 부분 초기값
    for express in expression[1:]: # -가 나온 부분 처리
        if "+" in express:
            result -= sum(list(map(int, express.split('+'))))
        else:
            result -= int(express)
print(result)