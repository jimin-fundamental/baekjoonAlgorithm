def solution(players, callings):
    name_to_idx = {name: idx for idx, name in enumerate(players)}  # 이름 → 인덱스

    for c in callings:
        num = name_to_idx[c]
        players[num], players[num - 1] = players[num - 1], players[num]

        # 인덱스 정보 업데이트
        name_to_idx[players[num]] = num
        name_to_idx[players[num - 1]] = num - 1

    return players
