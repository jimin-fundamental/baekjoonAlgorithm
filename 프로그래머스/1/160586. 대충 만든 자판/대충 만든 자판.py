def solution(keymap, targets):
    answer = []
    dic = {}
    for k in keymap:
        i = 0
        for a in k:
            i += 1
            if a not in dic:
                dic[a] = i
            else:
                if dic[a] > i:
                    dic[a] = i
    for target in targets:
        sumTarget = 0
        for a in target:
            if a in dic:
                sumTarget += dic[a]
            else:
                sumTarget = -1
                break
        answer.append(sumTarget)
        
    return answer