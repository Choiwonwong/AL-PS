# # Hash
N = int(input())
arr_n = set(list(map(int, input().split())))

M = int(input())
arr_m = list(map(int, input().split()))

for m in arr_m:
    if m in arr_n:
        print("1")
    else:
        print("0")

# Binary Search

def bs(target, arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        tmp = (left + right) // 2
        if arr[tmp] == target:
            return True
        elif arr[tmp] < target:
            left = tmp + 1
        else:
            right = tmp - 1   
    else:
        return False

N = int(input())
arr_n = list(map(int, input().split()))

M = int(input())
arr_m = list(map(int, input().split()))

arr_n.sort()

for m in arr_m:
    if bs(m, arr_n):
        print("1")
    else:
        print("0")