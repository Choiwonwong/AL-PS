T = int(input())
for _ in range(T):
    scores = list(input())
    seq = 0
    answer = 0
    for score in scores:
        if score == 'X':
            seq = 0
        else:
            seq += 1
            answer += seq
    print(answer)