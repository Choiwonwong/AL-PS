import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arrays = list(map(int, input().split()))
start = 1
end = max(arrays)
result = 0
def get_count(array, height):
    result = 0
    for a in array:
        if a > height:
            result += a - height
    return result
while start <= end:
    mid = (start + end) // 2
    mid_count = get_count(arrays, mid)
    if mid_count < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)