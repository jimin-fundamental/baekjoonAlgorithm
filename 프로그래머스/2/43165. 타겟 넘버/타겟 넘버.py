from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque([(0,0)])
    
    while q:
        idx, curr_sum = q.popleft()
        
        # 종료 조건
        if idx == len(numbers):
            if curr_sum == target:
                answer += 1
        else:
            # 다음 상태 전이
            q.append((idx+1, curr_sum + numbers[idx]))
            q.append((idx+1, curr_sum - numbers[idx]))
                
    return answer