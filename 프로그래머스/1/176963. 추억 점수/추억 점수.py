def solution(name, yearning, photo):
    answer = []
    key_map = {} #딕셔너리 사용
    for i in range(len(name)):
        key_map[name[i]] = yearning[i]
    for p in photo:
        a = 0
        for k in p:
            a += key_map.get(k, 0)  # 없는 이름은 0점
        answer.append(a)
    return answer