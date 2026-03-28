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
def solution(k, dungeons):
    answer = 0
    visited = [False]* len(dungeons)
    
    def dfs(current_k, count):
        nonlocal answer 
        
        # 종료 조건
        # 이 문제에서는 계속 answer을 기록하고
        # 모든 던전을 다 돌았거나 더이상 갈 곳이 없으면 자연스럽게 종료함
        answer = max(answer, count)
        
        if count == len(dungeons):
            return
        
        # 방문 가능한 곳 모두 방문
        for i in range(len(dungeons)):
             if not visited[i] and current_k >= dungeons[i][0]:
                    
                    # 방문 처리
                    visited[i] = True
                    
                    # 다음 상태로 전이
                    dfs(current_k - dungeons[i][1], count+1)
                    
                    # 백트래킹 
                    # - 다시 돌아왔을 때 다른 순서로도 돌 수 있게 방문 표시 해제
                    visited[i] = False
   # 초기 호출: 피로도 k, 탐험횟수 0에서 시작 
    dfs(k, 0)
    
    return answer
            