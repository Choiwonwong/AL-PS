# N 홀수
import sys
N = int(input())

arr = [int(int(sys.stdin.readline().rstrip())) for _ in range(N)]
arr.sort()
print(int(round(sum(arr)/N, 0)))
print(arr[N//2])

freq = {}
for a in arr:
    if a not in freq:
        freq[a] = 1
    else:
        freq[a] += 1
frequences = sorted(tuple(freq.items()), key= lambda x: [-x[1], x[0]])
if N > 1:
    if frequences[0][1] == frequences[1][1]:
        print(frequences[1][0])
    else:
        print(frequences[0][0])      
else:
    print(frequences[0][0])
print(arr[N-1] - arr[0])
