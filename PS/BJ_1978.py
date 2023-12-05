N = int(input())
arr = list(map(int, input().split()))
count = 0
for a in arr:
    is_prime = True
    for i in range(2, a):
        if a % i == 0:
            is_prime = False
            break
    if is_prime and a > 1:
        count += 1
print(count)