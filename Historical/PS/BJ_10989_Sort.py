# 딕셔너리를 통해 메모리 크기를 줄인 출력 수행
# 오름차순 정렬보다는 오름차순 출력을 수행함.
# 이런 저런 시도 수행
# pypy3으로 제출했음

# import sys
# N = int(sys.stdin.readline().rstrip())
# arr = {}
# for _ in range(N):
#     i = int(sys.stdin.readline().rstrip())
#     if i not in arr:
#         arr[i] = 1
#     else:
#         arr[i] += 1

# for key in sorted(list(arr.keys())):
#     for _ in range(arr[key]):
#         sys.stdout.write(str(key) + '\n')

# N = int(input())
# arr = {}
# for _ in range(N):
#     i = int(input())
#     if i not in arr:
#         arr[i] = str(i)
#     else:
#         arr[i] += str(i)

# for key in sorted(list(arr.keys())):
#     for s in arr[key]:
#         print(s)

# import sys
# N = int(input())
# arr = ["" for _ in range(10000)]
# for _ in range(N):
#     number = int(sys.stdin.readline().rstrip())
#     arr[number-1] += str(number)
    
# for a in "".join(arr):
#     sys.stdout.write(a + '\n')

import sys
N = int(sys.stdin.readline().rstrip())
arr = [0 for _ in range(10000)]
for _ in range(N):
    number = int(sys.stdin.readline().rstrip())
    arr[number-1] += 1
    
for i in range(10000):
    if arr[i] != 0:
        for j in range(arr[i]):
            sys.stdout.write(str(i+1) + '\n')