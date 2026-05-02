def solution(record):
    answer = []
    dic = {}
    
    # 각 uid의 최종 이름 판단 
    for r in record:
        op = r.split()[0]
        if op == "Enter" or op == "Change":
            uid = r.split()[1]
            name = r.split()[2]
            dic[uid] = name
    
    # 최종 이름으로 결과 출력
    for r in record:
        op = r.split()[0]
        uid = r.split()[1]
        name = dic[uid]
        
        if op == "Enter":
            s = name + "님이 들어왔습니다."
            answer.append(s)
        elif op == "Leave":
            s = name + "님이 나갔습니다."
            answer.append(s)
            
    
    return answer