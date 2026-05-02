def solution(n):
    answer = ''
    
    # 나머지가 0,1,2일 때의 값
    num = ["4", "1", "2"]
    
    while n > 0:
        remainder = n % 3
        
        answer = num[remainder] + answer
        
        if remainder == 0:
            n = n //3 - 1
        else: 
            n = n//3
    
    return answer