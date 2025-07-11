def solution(user_id, banned_id):
    # 1) 각 패턴별로 매칭 가능한 user_id 목록 만들기
    candidates = []
    for b in banned_id:
        matched = []
        for u in user_id:
            if len(b) != len(u):
                continue
            for uc, bc in zip(u, b):
                if bc != '*' and uc != bc:
                    break
            else:
                matched.append(u)
        candidates.append(matched)

    # 2) 백트래킹으로 가능한 조합 모두 생성
    results = set()
    def dfs(idx, path):
        if idx == len(candidates):
            # 정렬해서 튜플로 만들어 중복 제거
            results.add(tuple(sorted(path)))
            return
        for u in candidates[idx]:
            if u not in path:
                dfs(idx + 1, path + [u])

    dfs(0, [])
    # 3) 유니크한 조합의 개수 반환
    return len(results)
