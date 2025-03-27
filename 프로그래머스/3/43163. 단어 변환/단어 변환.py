from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0  # target이 없으면 종료

    visited = [0] * len(words)  # 각 단어 방문 여부 + 몇 단계째인지 저장
    queue = deque()
    queue.append((begin, 0))  # 시작 단어와 단계 수 함께 저장

    while queue:
        now, step = queue.popleft()  # 현재 단어와 지금까지 단계 수

        if now == target:
            return step  # 정답 도달

        for i in range(len(words)):
            if not visited[i] and is_convertible(now, words[i]):
                visited[i] = 1
                queue.append((words[i], step + 1))  # 다음 후보 넣기

    return 0  # target에 도달할 수 없는 경우

# 한 글자만 다른지 확인하는 함수
def is_convertible(word1, word2):
    diff = 0
    for a, b in zip(word1, word2):
        if a != b:
            diff += 1
        if diff > 1:
            return False
    return diff == 1
