# Stack 구현 및 처리
N = int(input())
target = [int(input()) for _ in range(N)]
stack = []
opers = []
idx = 1

for t in target:
    while idx <= t:
        stack.append(idx)
        opers.append("+")
        idx += 1

    if stack[-1] == t:
        stack.pop()
        opers.append("-")
    else:
        print("NO")
        exit(0)

for oper in opers:
    print(oper)