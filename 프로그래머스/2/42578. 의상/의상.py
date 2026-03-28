"""
- 서로 다른 옷의 조합 수 구하기
- 종류별로 최대 1가지 의상만 가능(안 입는 것도 가능)
- 옷을 하나는 입어야 됨

=>
각 type별 옷의 종류를 각각 구하기 [dict]
(각 type별 옷의 종류 + 1)끼리 곱하고 - 1(<- 아무것도 안 입는 경우)
"""
def solution(clothes):
    answer = 1
    
    # 각 type별 옷의 종류 가짓수 dict
    type = dict()
    
    for cloth in clothes:
        name = cloth[1]
        if type.get(name):
            type[name] += 1
        else:
            type[name] =1

    # 이들끼리 곱하기
    for i in type.values():
        answer *= (i+1)
    
    return answer-1