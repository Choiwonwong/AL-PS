import sys
N = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline()) for _ in range(N)] # input이냐 sys.stdin.readline이냐 차이..?
arr.sort()
for a in arr:
    print(a)