from itertools import permutations

def is_prime(num):
    """ 소수 판별 함수 """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    unique_numbers = set()  # 중복 제거를 위한 set

    # 가능한 모든 숫자 조합 만들기
    for length in range(1, len(numbers) + 1):
        for perm in permutations(numbers, length):
            num = int("".join(perm))  # 튜플을 문자열로 변환 후 정수 변환
            unique_numbers.add(num)  # 중복 제거하면서 저장

    # 소수 개수 세기
    return sum(1 for num in unique_numbers if is_prime(num))
