"""
피로도 시스템(0 이상의 정수)
 탐험을 시작하기 위해 필요한 "최소 필요 피로도"
 던전 탐험을 마쳤을 때 소모되는 "소모 피로도"
  던전들을 최대한 많이 탐험하려 함
  
  유저의 현재 피로도 k
  각 던전별 "최소 필요 피로도", "소모 피로도"가 담긴 2차원 배열 dungeons
  유저가 탐험할수 있는 최대 던전 수를 return 
  
  최대 8개니까 BF 가능 or DFS
"""
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for p in permutations(dungeons):
        current_k = k
        count = 0
        
        for (need, spend) in p :
            if current_k >= need:
                count += 1
                current_k -= spend
            else:
                break
        answer = max(answer, count)
        
    return answer
            