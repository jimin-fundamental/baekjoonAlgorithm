def solution(n):
    answer = 0
    a = 1
    for i in range(n):
        if n % a == 0:
            answer += a
        a += 1
    return answer