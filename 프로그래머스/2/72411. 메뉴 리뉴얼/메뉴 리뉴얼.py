from itertools import combinations

def solution(orders, course):
    answer = []
    
    for n in course:
        c = {}
        
        # 각 조합 주문된 횟수 세기
        for order in orders:
            for comb in combinations(order, n):
                s = ''.join(sorted(list(comb)))
                c[s] = c.get(s, 0) + 1
        
        # 만약 c가 비어있으면 패스
        if not c: 
            continue
            
        # 최대 value인 key answer에 추가
        max_value = max(c.values())
        
        if max_value < 2:
            continue
        
        for key, value in c.items():
            if value == max_value:
                answer.append(key)
    
    return sorted(answer)