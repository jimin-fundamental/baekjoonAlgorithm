def solution(nums):
    dic = {}
    numOfGet = len(nums)/2
    for name in nums:
        dic[name] = dic.get(name, 0) +1
    numOfType = len(dic)
    if numOfGet < numOfType:
        return numOfGet
    else:
        return numOfType
    
  