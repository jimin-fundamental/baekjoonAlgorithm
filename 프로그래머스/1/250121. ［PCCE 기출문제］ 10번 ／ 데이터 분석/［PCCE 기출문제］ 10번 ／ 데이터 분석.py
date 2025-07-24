def solution(data, ext, val_ext, sort_by):
    # ext와 sort_by에 따른 인덱스 매핑
    key_map = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }

    ext_index = key_map[ext]
    sort_index = key_map[sort_by]

    # 필터링: ext 값이 val_ext보다 작은 것만
    filtered = [d for d in data if d[ext_index] < val_ext]

    # 정렬: sort_by 기준 오름차순
    filtered.sort(key=lambda x: x[sort_index])

    return filtered
