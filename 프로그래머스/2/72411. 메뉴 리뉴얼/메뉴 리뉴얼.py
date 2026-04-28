from itertools import combinations

def solution(orders, course):
    answer = []
    
    dic = dict()
    
    for order in orders:
        n = len(order)
        
        for i in range(2, n+1): 
            # 모든 조합에 대해
            for comb in combinations(order, i):
                s = ''.join(sorted(comb))
                
                # dic에 넣기 
                dic[s] = dic.get(s, 0) + 1
    
    
    for c in course:
        candidate = []
        
        # 2번 이상 추천받은 리스트업
        for key, value in dic.items():
            if len(key) == c and value >= 2:
                candidate.append((value, key))
                
        # 최대로 추천받은 것 answer에 추가 
        candidate.sort(reverse = True)
        if len(candidate) > 0:
            maxvalue = candidate[0][0]
        print(candidate)
        
        for i in range(len(candidate)):
            if candidate[i][0] == maxvalue: 
                answer.append(candidate[i][1])
            else:
                break    
    
    return sorted(answer)