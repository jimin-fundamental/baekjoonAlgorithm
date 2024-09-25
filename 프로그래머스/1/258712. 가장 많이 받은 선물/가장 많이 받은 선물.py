def solution(friends, gifts):
    num_friend = len(friends)
    gift_list=[
        [0 for _ in range(num_friend)] for _ in range(num_friend)
    ]
    name_index = {}
    count = 0
    for friend in friends:
        name_index[friend] = count
        count += 1
        
    for gift in gifts:
        gift = gift.split()
        give = name_index[gift[0]]
        receive = name_index[gift[1]]
        gift_list[give][receive] += 1
        
    #선물지수 카운트
    gift_num = [0]*num_friend
    for i in range(num_friend):
        for k in range(num_friend):
            gift_num[i] += gift_list[i][k]
            gift_num[i] -= gift_list[k][i]
    
    #선물을 카운트
    result = [0]*num_friend
    for a in range(num_friend):
        for b in range(a+1, num_friend):
            """
            if a == b:
                break
            else:
            """
            num = gift_list[a][b] - gift_list[b][a]
            if num == 0:
                if gift_num[a] > gift_num[b]:
                    result[a] += 1
                elif gift_num[a] < gift_num[b]:
                    result[b] += 1 
            elif num > 0:
                result[a] += 1
            else:
                result[b] += 1
                    
    answer = max(result)
    return answer
