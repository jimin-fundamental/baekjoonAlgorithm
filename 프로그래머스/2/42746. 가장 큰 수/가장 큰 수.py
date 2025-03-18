def solution(numbers):
    # 붙였을 때 더 큰 값이 되는 걸로 정렬
    numbers = list(map(str,numbers))
    numbers.sort(key=lambda x: x*3, reverse = True)
    result = ''.join(numbers)
    return '0' if result[0] == '0' else result