def solution(s):
    answer = ''
    shouldBig = True
    for i in s:
        if shouldBig:
            answer += (i.upper())
        else:
            answer += i.lower()
        shouldBig = False
        if i == " ":
            shouldBig = "True"      
    return answer