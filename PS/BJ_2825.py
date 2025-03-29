import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)
while left < right:
    