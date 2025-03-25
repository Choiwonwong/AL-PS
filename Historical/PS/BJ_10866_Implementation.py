# Deque
# 일단 List로 해보고 안되면 Deque 사용
# push_front-> insert(n, 0)
# push_back-> append()
# pop_front -> pop(0) 없으면 -1
# pop_back -> pop() 없으면 -1
# size -> len()
# empty -> if stack으로 판단
# front -> [0] or -1
# back -> [-1] or -1
import sys

N = int(sys.stdin.readline().rstrip())
commands = [sys.stdin.readline().rstrip() for _ in range(N)]
deque = []
for command in commands:
    if command == "front":
        if deque:
            print(deque[0])
        else:
            print("-1")
    elif command == "back":
        if deque:
            print(deque[-1])
        else:
            print("-1")
    elif command == "empty":
        print(0 if deque else 1)
    elif command == "size":
        print(len(deque))
    elif command == "pop_front":
        if deque:
            print(deque.pop(0))
        else:
            print("-1")
    elif command == "pop_back":
        if deque:
            print(deque.pop())
        else:
            print("-1")
    else:
        expr, n = command.split()
        if expr == "push_back":
            deque.append(n)
        else:
            deque.insert(0, n)