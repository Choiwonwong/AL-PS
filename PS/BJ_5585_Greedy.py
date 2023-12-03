N = 1000 - int(input())
changes = [500, 100, 50, 10, 5, 1] # 거스름돈 단위
count = 0
for change in changes: # 큰 거스름돈부터 거슬러주기 시작
    count += N // change
    N = N % change
print(count)