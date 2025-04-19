
def solution(participant, completion):
    hash_map = {}
    for p in participant:
        if p in hash_map:
            hash_map[p] += 1
        else:
            hash_map[p] = 1
    for c in completion:
        hash_map[c] -= 1
    for n in hash_map:
        if hash_map[n] > 0:
            return n