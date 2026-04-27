import heapq

def solution(n, works):
    answer = 0
    heap = []
    
    for w in works:
        heapq.heappush(heap, -w)
    
    for _ in range(n):
        m = -heapq.heappop(heap)
        
        if(m > 0): m -= 1
        
        heapq.heappush(heap, -m)
                
    return sum([w**2 for w in heap])