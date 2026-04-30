def solution(weights):
    answer = 0
    
    # map 만들기
    dic = {}
    
    for w in weights:
        dic[w] = dic.get(w, 0) + 1
    
    # 몸무게 같은 경우
    for c in dic.values():
        if c >= 2:
            answer += c * (c-1) /2
            
    # 몸무게 2배, 2:3, 3:4 인 경우
    for w in dic.keys():
        if w*2 in dic.keys():
            answer += dic[w] * dic[w*2]
        if w*(3/2) in dic.keys():
            answer += dic[w] * dic[w*3/2]
        if w*(4/3) in dic.keys():
            answer += dic[w] * dic[w*4/3]
    
    return answer