def solution(book_time):
    answer = 1
    room = 1 #현재 남은 방의 개수 
    
    using = []
    
    # 입실 시간 순대로 정렬
    book_time.sort(key= lambda x:x[0])
    
    for start, end in book_time:
        # 분으로 환산
        s = start.split(":")
        start = int(s[0])* 60 + int(s[1])
        
        e = end.split(":")
        end = int(e[0])*60 + int(e[1])
        
        #시간 끝난 손님 내쫓기
        if len(using) > 0:
            for u in using:
                if u + 10 <= start:
                    using.remove(u) #이렇게 해도 문제 없나?
                    room += 1
        
        # 현재 방이 남았는지 체크하고 없으면 방 추가
        if room > 0:
            room -= 1
        else: 
            answer += 1
        
        using.append(end)

    return answer