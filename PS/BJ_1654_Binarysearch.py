K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

def count_lans(lines, length):
    count = 0
    for line in lines:
        count += line // length
    return count

def binary_search(lines, target):
    start, end = 1, max(lines)
    
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if count_lans(lines, mid) >= target:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

# 이분 탐색 수행
result = binary_search(lines, N)

print(result)