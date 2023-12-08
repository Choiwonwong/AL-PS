# Stack
while True:
    stack = []
    S = input()
    flag = False
    if S == '.':
        break
    for s in S:
        if s == '(':
            stack.append(s)
        elif s == '[':
            stack.append(s)
        elif s == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    flag = True
                    break
            else:
                flag = True
                break
        elif s == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    flag = True
                    break
            else:
                flag = True
                break
    if flag or stack:
        print("no")
    else:
        print("yes")