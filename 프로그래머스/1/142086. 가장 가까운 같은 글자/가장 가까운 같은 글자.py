def solution(s):
    answer = []
    for i in range(len(s)):
        say = True
        for m in range(i-1,-1,-1):
            if s[i] == s[m]:
                answer.append(i-m)
                say = False
                break
            
        if say:
            answer.append(-1)
    return answer