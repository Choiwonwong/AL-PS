# Brute Force
# 666이 들어가있기만 하면 그만

N = int(input())
count = 0
idx = 666
while count < N:
    if '666' in str(idx):
        count += 1
    idx += 1
else:
    idx -= 1
print(idx)