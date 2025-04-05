from collections import deque

def solution(numbers, target):
    answer = 0
    
    def dfs(index, current_sum):
        nonlocal answer #함수 밖에서 정의한 변수를 안에서 사용하고 싶을 때 이런 식으로 재정의
        if index == len(numbers):
            if current_sum == target:
                answer += 1
            return #target이 아니어도, return해야 다음으로 넘어갈 수 있음
        
        dfs(index+1, current_sum + numbers[index]) 
        dfs(index+1, current_sum - numbers[index])
    
    dfs(0, 0)
    
    return answer