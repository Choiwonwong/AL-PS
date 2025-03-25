import sys
N = int(input())
sets = []
for _ in range(N):
    statments = sys.stdin.readline().lstrip()
    if "add" in statments:
        value = int(statments.split()[-1])
        if value not in sets:
            sets.append(value)
    elif "check" in statments:
        value = int(statments.split()[-1])
        print(int(value in sets))
    elif "toggle" in statments:
        value = int(statments.split()[-1])
        if value not in sets:
            sets.append(value)
        else:
            idx = sets.index(value)
            sets.pop(idx)
    elif "remove" in statments:
        value = int(statments.split()[-1])
        if value in sets:
            idx = sets.index(value)
            sets.pop(idx)
    elif "empty" in statments:
        sets.clear()
    else:
        sets = [i for i in range(1, 21)]