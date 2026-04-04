def solution(gems):
    total_kinds = len(set(gems)) # 보석의 총 종류 수
    n = len(gems)
    answer = [1, n] # 가장 긴 구간으로 초기화
    
    current_items = {} # 현재 구간의 보석 개수를 담을 딕셔너리
    left = 0
    min_len = n + 1
    
    for right in range(n):
        # 1. 오른쪽 보석을 추가
        current_items[gems[right]] = current_items.get(gems[right], 0) + 1
        
        # 2. 모든 종류의 보석이 구간 안에 들어왔다면?
        while len(current_items) == total_kinds:
            # 3. 최단 구간 갱신 (더 짧거나, 같으면 시작 인덱스가 작은 것)
            if right - left < min_len:
                min_len = right - left
                answer = [left + 1, right + 1]
            
            # 4. 왼쪽 보석을 하나 빼보며 구간 줄이기
            current_items[gems[left]] -= 1
            if current_items[gems[left]] == 0:
                del current_items[gems[left]] # 개수가 0이 되면 종류에서 삭제
            left += 1
            
    return answer