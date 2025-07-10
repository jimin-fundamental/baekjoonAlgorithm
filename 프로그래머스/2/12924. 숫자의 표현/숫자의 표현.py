def solution(n):
    count = 0  # 가능한 표현의 수를 세는 변수
    k = 1      # 연속된 자연수의 개수 (k = 1부터 시작)
    while k * (k - 1) // 2 < n:   # n보다 작을 때까지만 반복
        if (n - k * (k - 1) // 2) % k == 0:
            count += 1
        k += 1
    return count
