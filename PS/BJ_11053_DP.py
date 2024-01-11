# 가장 긴 증가하는 부분 수열

def longest_increasing_subsequence(n, arr):
    lis = [1] * n

    for i in range(1, n): # 1 ~ N개의 원소들의 최장 증가 순열의 길이를 계산한다.
        for j in range(i): # 이전 원소들을 탐색 -> N번째 이전 원소들 전부
            # 현재 원소가 이전 원소보다 크고, 현재 LIS 길이가 이전 LIS 길이보다 작을 때
            if arr[i] > arr[j] and lis[i] < lis[j] + 1: 
                lis[i] = lis[j] + 1 # LIS 길이를 업데이트
    return lis

n = int(input())
arr = list(map(int, input().split()))

print(max(longest_increasing_subsequence(n, arr)))