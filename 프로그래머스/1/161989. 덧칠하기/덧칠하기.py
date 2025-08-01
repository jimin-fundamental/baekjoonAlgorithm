def solution(n, m, section):
    count = 0
    i = 0
    
    while i < len(section):
        # 현재 section[i]부터 롤러를 칠함
        start = section[i]
        end = start + m - 1
        
        # 다음 칠해야 할 section이 롤러 범위를 벗어날 때까지 i 증가
        while i < len(section) and section[i] <= end:
            i += 1
        
        count += 1

    return count
