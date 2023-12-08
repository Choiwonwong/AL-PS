# List로 구현하자.

T = int(input())
for _ in range(T):
    N, M =map(int, input().split())
    prioritys = list(map(int, input().split()))
    sequence = []
    for i, priority in enumerate(prioritys):
        sequence.append((i, priority))
    count = 0
    while sequence:
        cur = sequence.pop(0)
        checks = [ cur[1] < seq[1] for seq in sequence]
        if checks.count(True):
            sequence.append(cur)
        else:
            count += 1
            if cur[0] == M:
                print(count)
                break   