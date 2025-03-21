def solution(participant, completion):
    p = {}
    for name in participant:
        p[name] = p.get(name,0) +1
    for name in completion:
        p[name] -= 1
    for name in p:
        if p[name] >0 :
            return name
    
            