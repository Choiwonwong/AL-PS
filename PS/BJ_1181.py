N = int(input())
words = list(set([input() for _ in range(N)]))
for word in sorted(words, key=lambda x:[len(x), x]):
    print(word)