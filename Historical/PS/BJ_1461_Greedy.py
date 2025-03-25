# 책을 모두 제자리에 둘 때 걸리는 최소 걸음 수
# 책의 위치는 음수도 있다.
# 책을 모두 제자리에 놓고 나서는 돌아올 필요는 없다. -> 맨 마지막에는 안돌아와도됨.

# 방향을 먼저 결정해야하나?
# 가장 먼 거리를 가장 나중에 하는 것이 맞음, 그리고 2개를 가져가야함 -> 안돌아와도 되니깐

N, M = map(int, input().split())
books = list(map(int, input().split()))
posi_books = []
nega_books = []
for book in books:
    if book > 0:
        posi_books.append(book)
    else:
        nega_books.append(book)

posi_books.sort()
nega_books.sort(reverse=True)
steps = 0

if posi_books[-1] + nega_books[-1] > 0:
    steps += posi_books[-1]
    for _ in range(M):
        if posi_books:
            posi_books.pop()
elif posi_books[-1] + nega_books[-1] < 0:
    steps += nega_books[-1]
    for _ in range(M):
        if nega_books:
            nega_books.pop()
else:
    if len(posi_books) >= len(nega_books):
        steps += posi_books[-1]
        for _ in range(M):
            if posi_books:
                posi_books.pop()
    else:
        steps += posi_books[-1]
        for _ in range(M):
            if nega_books:
                nega_books.pop()
print(posi_books, nega_books)
print(steps)