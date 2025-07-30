def solution(x):
    answer = True
    s = 0
    x = str(x)
    for i in range(len(x)):
        s += int(x[i])
    
    if int(x) % s == 0:
        return True
    else:
        return False
    return answer