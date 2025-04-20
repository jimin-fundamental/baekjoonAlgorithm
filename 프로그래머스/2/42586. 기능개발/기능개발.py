#각 기능은 진도가 100%일 때 서비스에 반영
#각 기능의 개발속도는 모두 다름
# 하루에 한번 배포
# progresses = 배포해야되는 순서대로 작업의 진도가 적힌 
# 뒤의 기능은 앞에 있는 기능이 다 배포되어야 배포
# speeds = 각 작업의 개발 속도
# return: 각 배포마다 몇 개의 기능이 배포되는지
from collections import deque

def solution(progresses, speeds):
    #하루씩 돌면서 오늘 끝내지는 게 있는지 확인(progresses >= 100) -> 두 list에서 모두 삭제 / 따로 이미 끝난 앤지 체크하는 배열 
    answer = []
    q = deque(progresses)
    s= deque(speeds)
        
    while q: #모든 작업이 끝나질 때까지 
        count = 0
        for i in range(len(q)): #오늘의 작업
            q[i] += s[i]
            
        while q and (q[0] >= 100):
            q.popleft()
            s.popleft()
            count += 1
            
        if count > 0:
            answer.append(count)
    return answer
