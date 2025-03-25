import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
not_listen = set()
not_see = set()
for i in range(N):
    not_listen.add(sys.stdin.readline().rstrip())
for i in range(M):
    not_see.add(sys.stdin.readline().rstrip())
not_listen_see = sorted(list(not_listen & not_see))
print(len(not_listen_see))
for i in not_listen_see:
    print(i)

# python PS\BJ_1620.py