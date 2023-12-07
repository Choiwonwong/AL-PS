T = int(input())
for _ in range(T):
    S = input()
    stack = []
    answer = ""
    for s in S:
        if stack:
            if s == ")" and stack[-1] == "(":
                stack.pop()
                continue
        stack.append(s)
    if stack:
        print("NO")
    else:
        print("YES")