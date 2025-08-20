def solution(priorities, location):
    answer = 0
    while priorities:
        newOne = priorities.pop(0)
        location -= 1
        
        if any(p > newOne for p in priorities):
            priorities.append(newOne)
            if location < 0:
                location = len(priorities) -1
        
        else:
            answer += 1
            if location < 0 :
                return answer
  