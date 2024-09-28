def solution(words):
    odd = ""
    half_p =""
    
    #개수 파악
    counts = {}
    
    for i in range(len(words)):
        word = words[i]
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    
    for alp in sorted(counts.keys()):
        if counts[alp] % 2 ==1:
            if odd:
                return "I'm Sorry Hansoo"
            odd = alp
        half_p += alp * (counts[alp] // 2)
    
    answer = half_p + odd + half_p[::-1]
    return answer
            
        




#n,k = tuple(map(int, input().split()))
#n = int(input())
#p = list(map(int, input().split()))
words = input()
print(solution(words))