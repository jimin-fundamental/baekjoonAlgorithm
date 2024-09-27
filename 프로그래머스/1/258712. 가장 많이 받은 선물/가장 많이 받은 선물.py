def solution(friends, gifts):
    n = len(friends)
    # 친구 간 선물 준 기록
    gift_count = {friend: {other: 0 for other in friends} for friend in friends}
    
    # 기록 넣기
    for gift in gifts:
        giver, receiver = gift.split()
        gift_count[giver][receiver] += 1
        
    # 선물지수 계산
    gift_index = {me: sum(gift_count[me].values()) - sum(gift_count[other][me] for other in friends) for me in friends}
    
    result = {friend: 0 for friend in friends}
    
    # 선물 주고받기 생각
    for q in range(n):
        for p in range(q+1, n):
            a = friends[q]
            b = friends[p]
            
            if gift_count[a][b] > gift_count[b][a]:
                result[a] += 1
            elif gift_count[a][b] < gift_count[b][a]:
                result[b] += 1
            else:
                if gift_index[a] > gift_index[b]:
                     result[a] += 1
                elif gift_index[a] < gift_index[b]:
                     result[b] += 1   
    
    answer = max(result.values())
    
    return answer