def solution(survey, choices):
    answer = ''
    score = [4]*4
    howMany = [1]*4
    # scoreB = [0]*4
    # howManyB = [1]*4
    
    a = ["R", "C", "J", "A"]
    b = ["T", "F", "M", "N"]
    
    for i in range(len(survey)):
        second = survey[i][1]
        if second in a:
            score[a.index(second)] += choices[i]
            howMany[a.index(second)] += 1
        else:
            score[b.index(second)] += 8 - choices[i]
            howMany[b.index(second)] += 1
        
    for i in range(len(score)):
        trueScore = score[i] / howMany[i]
        if (trueScore)  >= 4:
            answer += a[i]
        else:
            answer += b[i]
    
    return answer