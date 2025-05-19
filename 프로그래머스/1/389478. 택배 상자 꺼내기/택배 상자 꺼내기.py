def solution(n, w, num):
    answer = 0
    boxes = [[] for _ in range(w)]
    
    where = 0 
    right = True
    
    # 일단 담기
    for i in range(1, n+1):
        boxes[where].append(i)
        if right: 
            if where <= w-2: # where= 0 ~ w-1(0 ~ w-2)
                where += 1
            else:
                right = False
        else:
            if where > 0: # where= 0 ~ w-1(1~w-1)
                where -= 1
            else:
                right = True
                
    # 찾기
    for b in range(w):
        if num in boxes[b]:
            while boxes[b]:
                answer += 1
                if boxes[b].pop() == num:
                    return answer
                    