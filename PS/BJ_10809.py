S = input()
counts = [-1 for _ in range(ord('a'), ord('z')+1)]

for i in range(len(S)):
    idx = ord(S[i]) - ord('a')
    if counts[idx] == -1:
        counts[idx] = i
for c in counts:
    print(c, end=" ")