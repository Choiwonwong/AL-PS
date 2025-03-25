N, M = map(int, input().split())
packages = []
eaches = []
for _ in range(M):
    package, each = map(int, input().split())
    packages.append(package)
    eaches.append(each)

package_cost = min(packages) # 가장 싼 패키지
each_cost = min(eaches) # 가장 싼 단품
cost = 0
if each_cost * 6 < package_cost: # 만약, 단품으로 사는게 제일 쌀 때
    cost = N * each_cost
else:
    if N % 6 * each_cost < package_cost:  # 패키지로 사고 남은 건 단품으로 살 때
        cost = N // 6 * package_cost + N % 6 * each_cost
    else: # 패키지로 사고 남은 단품의 가격이 패키지 값보다 비쌀 때
        cost = (N // 6 + 1) * package_cost
print(cost)