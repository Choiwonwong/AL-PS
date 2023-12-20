# 어거지로 구현,,
from itertools import combinations
import sys
input = sys.stdin.readline

def get_distance(a, b): # 거리 계산 함수
    distance = 0
    for i in range(4):
        if a[i] != b[i]:
            distance += 1
    return distance

T = int(input())
for _ in range(T):
    N = int(input())
    mbtis = input().split()

    mbti_dict = {} # 딕셔너리로 MBTI별 인원 수를 계산
    for mbti in mbtis:
        if mbti not in mbti_dict:
            mbti_dict[mbti] = 1
        else:
            mbti_dict[mbti] += 1

    max_value = max(mbti_dict.values()) # 최대 수에 따라서 분기 처리
    if max_value >= 3: # 3명 이상이 같으면 0
        print(0)
    else: # 2명이 있을 때와 없을 때를 포괄해서 계산 
        result = 16
        two_mbtis = [] # 2명이 있는 경우 계산
        for mbti, count in mbti_dict.items():
            if count == 2:
                two_mbtis.append(mbti)
        for a in two_mbtis:
            for b in mbti_dict.keys():
                if a != b:
                    result = min(result, 2*get_distance(a, b))

        for combi in combinations(mbti_dict.keys(), 3): # 세명이 모두 다를 경우도 계산
            tmp = 0
            if len(set(combi)) == 2:
                for a, b in set(combi):
                    tmp += 2* get_distance(a, b)
            else:
                for a, b in combinations(combi, 2):
                    tmp += get_distance(a, b)
            result = min(result, tmp)
        print(result)