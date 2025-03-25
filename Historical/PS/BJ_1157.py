S = list(input().upper())
counts = [0 for _ in range(ord('A'), ord('Z')+1)]

for s in S:
    idx = ord(s) - ord('A')
    counts[idx] += 1

if counts.count(max(counts)) >= 2:
    print('?')
else:        
    print(chr(ord('A') + counts.index(max(counts))))