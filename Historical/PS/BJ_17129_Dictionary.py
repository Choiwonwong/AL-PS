import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
dictionary = {}
for i in range(N):
    site, passwd = sys.stdin.readline().rstrip().split()
    dictionary[site] = passwd
for i in range(M):
    print(dictionary[sys.stdin.readline().rstrip()])