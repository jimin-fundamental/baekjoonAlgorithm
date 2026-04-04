def solution(money):
    # 집이 3개 미만인 경우는 제한사항에 없지만 예외 처리를 해두면 안전합니다.
    if len(money) == 3:
        return max(money)

    # 1. 첫 번째 집을 무조건 터는 경우 (마지막 집 제외)
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    
    for i in range(2, len(money) - 1): # 마지막 집 전까지만!
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
        
    # 2. 첫 번째 집을 안 터는 경우 (마지막 집 포함 가능)
    dp2 = [0] * len(money)
    dp2[0] = 0 # 첫 집은 0
    dp2[1] = money[1]
    
    for i in range(2, len(money)): # 끝까지!
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
        
    # 두 시나리오 중 최댓값 반환
    return max(max(dp1), max(dp2))