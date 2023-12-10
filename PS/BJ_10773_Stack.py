# Stack
import sys
N = int(sys.stdin.readline().lstrip())
stack = []
for _ in range(N):
    n = int(sys.stdin.readline().lstrip())
    if n == 0:
        if stack:
            stack.pop()
    else:
        stack.append(n)
print(sum(stack))
