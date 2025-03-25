N = input()
N_to_0 = []
N_to_1 = []

for tmp in N.split('1'): # 0으로 바꾸는 횟수
    if tmp != '':
        N_to_0.append(tmp)

for tmp in N.split('0'): # 1으로 바꾸는 횟수
    if tmp != '':
        N_to_1.append(tmp)

print(min(len(N_to_0), len(N_to_1))) # 그 중 최솟값