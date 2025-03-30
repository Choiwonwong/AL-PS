# N = 100
# for _ in range(N):
#     input_str = input()
#     if input_str != "":
#         print(input_str)
#     else:
#         break

# import sys
# input_strs = sys.stdin.readlines()
# print(input_strs)

import sys

# input_strs = sys.stdin.readlines()
# for input_str in input_strs:
#     print(input_str.strip())
# 이렇게 사용하면 마지막에 Enter가 아니라 Ctrl + D 같은 EOF를 입력해야함.

import sys
print(sys.stdin.read()) # 이거는 리스트로 담지도 않고 정말 똑같이 담고 있움.