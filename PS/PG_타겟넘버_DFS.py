def solution(numbers, target):
    answer = [0] # 최초 겂 초기화
    
    def dfs(index, current):
        if index == len(numbers): # 끝까지 도달했을 때
            if current == target: # 값을 만들 수 있으면
                answer[0] += 1 # 결과 +1
        else: # 도달하지 않았으면
            dfs(index+1, current + numbers[index]) # + 경우 한단계 +1
            dfs(index+1, current - numbers[index]) # - 경우 한단계 +1
    dfs(0, 0)    
    return answer[0]