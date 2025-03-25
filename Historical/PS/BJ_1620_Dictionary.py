import sys

N, M = map(int, sys.stdin.readline().lstrip().split())
dict1 = {}
dict2 = {}
for i in range(N):
    name = sys.stdin.readline().rstrip()
    dict1[name] = i + 1
    dict2[i+1] = name
for _ in range(M):
    problem = sys.stdin.readline().rstrip()
    if problem in dict1:
        print(dict1[problem])
    else:
        print(dict2[int(problem)])

# python PS\BJ_1620.py