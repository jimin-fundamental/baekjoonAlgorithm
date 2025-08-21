def solution(n):
    for x in range(2, n):   # 1은 항상 나머지가 0이므로 2부터 시작
        if n % x == 1:
            return x
