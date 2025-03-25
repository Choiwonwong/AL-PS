# O(N) -> X O(logN) 복잡도를 사용한 탐색 필요
# 8의 위치가 같은 개수를 세면 됨.
# 앞에서부터 몇개의 prefix 같은지를 체크하고, 그 중에 8의 개수를 세면 됨

L, R = input().split()
answer = 0
if len(L) == len(R):
    for i in range(len(L)):
        if L[i] == R[i]:
            if L[i] == '8':
                answer += 1
        else:
            break
print(answer)