from collections import defaultdict
import heapq
def solution(operations):
    max_heap = []
    min_heap = []
    dic = defaultdict(int)
    for op in operations:
        if op[0] == "I":
            num = int(op[2:])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            dic[num] += 1
        else:
            if not any(v >0 for v in dic.values()):
                continue
            else:
                if op == "D 1": #최댓값 삭제
                    while max_heap: 
                        num = -heapq.heappop(max_heap)
                        if dic[num] <= 0: #가능하지 않은 숫자
                            continue 
                        else:
                            break
                    dic[num] -= 1
                else: #최솟값 삭제
                    while min_heap: 
                        num = heapq.heappop(min_heap)
                        if dic[num] <= 0:
                            continue
                        else:
                            break
                    dic[num] -= 1
    if not any(v >0 for v in dic.values()):
        return [0,0]
    while max_heap: 
        num = -heapq.heappop(max_heap)
        if dic[num] <= 0:
            continue
        else:
            break
    realMax = num
    while min_heap: 
        num = heapq.heappop(min_heap)
        if dic[num] <= 0:
            continue
        else:
            break
    realMin = num
    return [realMax, realMin]