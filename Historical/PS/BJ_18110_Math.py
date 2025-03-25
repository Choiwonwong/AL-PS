# 정렬 및 수학
import sys

def custom_round(n): # 오사오입을 거른다.
    s = str(n)
    if '.5' in s:
        ns = int(s.split('.')[0])
        if ns % 2 == 0:
            result = round(n, 0) + 1
        else:
            result = round(n, 0)
    else:
        result = round(n, 0)
    return result

N = int(sys.stdin.readline().rstrip())
if N == 0:
    print(0)
    exit()
difficulties = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
outs = int(custom_round(N * 0.15))
if outs == 0:
    print(int(custom_round(sum(difficulties)/N)))
else:
    difficulties.sort()
    print(int(custom_round(sum(difficulties[outs: -outs])/(N-2*outs))))