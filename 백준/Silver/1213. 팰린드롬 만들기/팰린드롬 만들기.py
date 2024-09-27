def solution(words):
    half_p =""
    count = {}
    odd = ""
    answer = ""
    for char in words:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    #char - 알파벳 / count[char] - 숫자
    for char in sorted(count.keys()):
        if count[char] % 2 ==1:
            if odd:
                return "I'm Sorry Hansoo"
            odd = char
        half_p += char*(count[char]//2)
        
    answer = half_p + odd +half_p[::-1]   
    return answer

#a,b = tuple(map(int, input().split()))
#n = int(input())
#p = list(map(int, input().split()))
words = input()
print(solution(words))