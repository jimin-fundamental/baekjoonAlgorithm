def solution(X, Y):
    # 숫자 개수를 저장할 딕셔너리
    x_count = {}
    y_count = {}

    # X에서 각 숫자의 개수 저장
    for digit in X:
        if digit in x_count:
            x_count[digit] += 1
        else:
            x_count[digit] = 1

    # Y에서 각 숫자의 개수 저장
    for digit in Y:
        if digit in y_count:
            y_count[digit] += 1
        else:
            y_count[digit] = 1

    # 공통 숫자를 저장할 리스트
    common_numbers = []

    for digit in x_count:
        if digit in y_count:
            # ✅ y_count(digit) → y_count[digit]로 수정
            common_numbers.extend([digit] * min(x_count[digit], y_count[digit]))

    # ❌ 이 부분이 잘못됨: 공통 숫자가 없을 때 검사하는 코드가 잘못된 위치에 있음.
    # ✅ 올바른 위치로 이동해야 함
    if not common_numbers:
        return "-1"

    # 내림차순 정렬 (가장 큰 수 만들기)
    common_numbers.sort(reverse=True)

    # 리스트를 문자열로 변환
    result = "".join(common_numbers)

    # 0으로만 구성된 경우 "0" 반환
    return "0" if result[0] == "0" else result
