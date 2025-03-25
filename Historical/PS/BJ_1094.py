import sys
input = sys.stdin.readline

X = int(input())

bars = [64]
while True:
    if sum(bars) == X:
        break
    if sum(bars) > X:
        tmp = bars.pop()
        bars.append(tmp//2)
        if sum(bars) < X:
            bars.append(tmp)
print(len(bars))
            



    

    



