def solution(survey, choices):
    answer = ''
    personality = {char: 0 for char in "RTCFJMAN"}
    score_map = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    
    for i in range(len(survey)):
        first, second = survey[i]
        choice = choices[i]
        if choice <4:
            personality[first] += score_map[choice]
        elif choice >4:
            personality[second] += score_map[choice]
        
    answer += "R" if personality["R"] >= personality["T"] else "T"
    answer += "C" if personality["C"] >= personality["F"] else "F"
    answer += "J" if personality["J"] >= personality["M"] else "M"
    answer += "A" if personality["A"] >= personality["N"] else "N"
    
    
    return answer