def solution(quiz):
    answer = []
    for q in quiz:
        list = q.split()
        X = int(list[0])
        Y = int(list[2])
        Z = int(list[4])
        operator = list[1]
        if operator == "+":
            result = X+Y
        else:
            result = X-Y
        if result == Z:
            answer.append("O")
        else:
            answer.append("X")
            
        
        
    return answer