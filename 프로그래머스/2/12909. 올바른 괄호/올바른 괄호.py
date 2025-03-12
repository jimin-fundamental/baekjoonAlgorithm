def solution(s):
    sum = 0
    for i in range(1, len(s) +1):
        if(s[-i] == ')'):
            sum += 1
        elif(s[-i] == '('):
            sum -= 1
        if(sum <0):
            return False
    
    if(sum == 0):
        return True
    else:
        return False
    
    
