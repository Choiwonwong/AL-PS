# 사전 순으로 가장 빠른 문자열을 만들 수 있는 방법이 무엇일까?

# 다음 카드를 선택할 때마다, 비교해서 집어넣기

T = int(input())
for _ in range(T):
    N = int(input())
    S = list(input().split())
    answer = S[0]
    for s in S[1:]:
        front_case = s + answer
        back_case = answer + s
        answer = front_case if front_case < back_case else back_case
    print(answer)