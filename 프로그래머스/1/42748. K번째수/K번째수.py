def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        
        newArray = array[i-1:j]
        newArray.sort()
        answer.append(newArray[k-1])
    
    return answer