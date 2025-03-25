N = int(input())
dice = list(map(int, input().split()))

triple_list = []
double_list = []
one_value = min(dice)

triple_indexes = [ # 세 면에 해당하는 경우의 수
    [0,1,2], [0,1,3],
    [0,2,4], [0,3,4],
    [1,2,5], [1,3,5],
    [2,4,5], [3,4,5]
]

double_indexes = [ # 두 면에 해당하는 경우의 수
    [0, 1],[0, 2],
    [0, 3],[0, 4],
    [1, 2],[1, 3],
    [1, 5],[2, 4],
    [2, 5],[3, 4],
    [3, 5],[4, 5]
]

for triple_index in triple_indexes: # 세 면에 해당하는 경우의 수의 합 
    triple_list.append(sum(dice[i] for i in triple_index))

for double_index in double_indexes: # 두 면에 해당하는 경우의 수의 합 
    double_list.append(sum(dice[i] for i in double_index))

result = 0
result += min(triple_list) * 4 # 세 면
result += min(double_list) * (4 * (N-2) + 4 * (N-1)) # 두 면
result += one_value * (4 * ((N-2)** 2 + N-2 ) + (N-2)**2 ) # 한 면

if N == 1: # 한개의 주사위일 경우
    dice.sort()
    result = sum(dice[:-1])

print(result)