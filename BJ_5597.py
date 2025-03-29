students = set([i for i in range(1, 31)])
result = set()
for _ in range(28):
    number = int(input())
    result.add(number)

for a in sorted(list(students - result)):
    print(a)