from itertools import product

def solution(word):
    vowels = [ 'A', 'E', 'I', 'O', 'U']
    dic = []
    
    for i in range(1, 6):
        for p in product(vowels, repeat = i):
            dic.append("".join(p))
    
    dic.sort()
    
    return dic.index(word)+1
    
    
        