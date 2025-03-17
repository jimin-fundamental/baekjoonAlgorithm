def solution(ingredient):
    answer = 0
    # 스택 사용
    stack = []
    for item in ingredient:
        stack.append(item)
        if stack[-4:] == [1,2,3,1]:
            answer += 1
            del stack [-4:]
    
    return answer