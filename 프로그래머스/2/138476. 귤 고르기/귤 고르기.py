import heapq

def solution(k, tangerine):
    answer = 0
    dic = dict()
    
    for t in tangerine:
        dic[t] = dic.get(t, 0) + 1
    
    c = 0
    
    heap = []
    
    for value in dic.values():
        heapq.heappush(heap, -value)
        
    
    while c < k:
        cur = -heapq.heappop(heap)
        c += cur
        answer += 1
    
    return answer