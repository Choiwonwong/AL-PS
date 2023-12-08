# Queue
# 일단 List로 해보고 안되면 Deque 사용
# Push -> append()
# Pop -> 없으면 -1
# size -> len()
# empty -> if stack으로 판단
# front -> [0] or -1
# back -> [-1] or -1
import sys

N = int(sys.stdin.readline().rstrip())
commands = [sys.stdin.readline().rstrip() for _ in range(N)]
queue = []
for command in commands:
    if command == "front":
        if queue:
            print(queue[0])
        else:
            print("-1")
    elif command == "back":
        if queue:
            print(queue[-1])
        else:
            print("-1")
    elif command == "empty":
        print(0 if queue else 1)
    elif command == "size":
        print(len(queue))
    elif command == "pop":
        if queue:
            print(queue.pop(0))
        else:
            print("-1")
    else:
        expr, n = command.split()
        queue.append(n)