def solution(s, skip, index):
    answer = ''
    new_skip = []
    for sk in skip:
        new_skip.append(ord(sk))
        
    for letter in s:
        get_letter = ord(letter)
        for i in range(index):
            get_letter += 1
            
            if get_letter > ord('z'):
                get_letter = ord('a')
            
            # check its in new_skip
            while get_letter in new_skip:
                get_letter += 1
                
                if get_letter > ord('z'):
                    get_letter = ord('a')

            
        #반영해서 더해주기
        answer += chr(get_letter)
        
    return answer