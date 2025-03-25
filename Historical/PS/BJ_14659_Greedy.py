# 자신의 우측에 자신의 값보다 작은 원소의 개수가 가장 많은 개수를 출력한다. 

N = int(input())
archors = list(map(int, input().split()))

tmp = archors[0]
counts = 0
answer = 0
for archor in archors[1:]:
    if archor > tmp:
        answer = max(counts, answer)
        counts=0
        tmp = archor
    else:
        counts+=1
print(max(answer, counts))