import math

def solution(r1, r2):
    answer = 0

    for y in range(1, r2 + 1):
        max_x = int(math.floor(math.sqrt(r2**2 - y**2)))
        min_x = 0 if y > r1 else int(math.ceil(math.sqrt(max(0, r1**2 - y**2))))

        count = max_x - min_x + 1
        if count > 0:
            answer += count

    answer *= 4  # 1사분면만 계산했으므로 *4
    return answer
