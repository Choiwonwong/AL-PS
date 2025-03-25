# Stack
# Push -> append()
# Pop -> 없으면 -1
# size -> len()
# empty -> if stack으로 판단
# top -> if stack으로 판단.

N = int(input())
commands = [input() for _ in range(N)]
stack = []
for command in commands:
    if command == "top":
        if stack:
            print(stack[-1])
        else:
            print("-1")
    elif command == "empty":
        print(0 if stack else 1)
    elif command == "size":
        print(len(stack))
    elif command == "pop":
        if stack:
            print(stack.pop())
        else:
            print("-1")
    else:
        expr, n = command.split()
        stack.append(n)