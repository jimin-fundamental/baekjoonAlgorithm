"""
- N마리 중 N/2마리 가져감
- 종류에 따라 번호 
- 같은 종류라도 이를 구분
- 최대한 많은 종류 가지고 싶음 
- nums: N마리 폰켓몬의 종류 번호 담긴 배열 
=> 각 번호가 몇 마리씩인지 dict로 정리 
N/2 < len(dict) -> N/2 가짓수
N/2 >= len(dict) -> len(dict) 가짓수

"""

def solution(nums):
    answer = 0
    N = len(nums)
    
    # dict 만들기
    types = dict()
    
    for num in nums:
        if num in types.keys():
            types[num] += 1
        else:
            types[num] = 1
    
    # 가짓수 return
    if N/2 < len(types):
        answer = N/2
    else:
        answer = len(types)
            
    return answer