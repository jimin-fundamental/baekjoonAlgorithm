def solution(k, m, score):
    answer = 0
    score.sort()
    while True:
        box = []
        a = 0
        for i in range(m):
            if(len(score) >0):
                a = score.pop()
            else:
                return answer
            box.append(a)
        answer += a*m
    