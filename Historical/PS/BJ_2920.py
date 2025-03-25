notes = list(map(int, input().split()))
ascend = [i for i in range(1, 9)]
if notes == ascend:
    answer = "ascending"
elif notes == ascend[::-1]:
    answer = "descending"
else:
    answer = "mixed"
print(answer)