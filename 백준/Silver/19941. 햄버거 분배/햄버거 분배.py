def solution(n,k,string):
    eat = 0
    #사람이 앉아있는 곳
    people = []
    burger = []
    for i in range(len(string)):
        if string[i] == 'P':
            people.append(i)
        else:
            burger.append(i)
    
    burger_set = set(burger)  # 빠른 탐색을 위해 버거 위치를 set으로 저장        
    
    for loc in people:
        didEat = False
        # 왼쪽
        for a in range(k,0, -1):
            check = loc - a #
            if check in burger_set:
                eat += 1
                didEat = True
                # burger list에서 check 숫자를 없애야 됨
                burger_set.remove(check) 
                break
        # 오른쪽은 제일 가까운 것부터 먹어야 되는듯
        if didEat ==False:
            for a in range(1,k+1):
                check = loc + a
                if check in burger_set:
                    eat += 1
                    # burger list에서 check 숫자를 없애야 됨 - burger.remove(check)를 사용하면 특정 값을 찾아 삭제
                    burger_set.remove(check)
                    break
            
    answer = eat
    return answer

a,b = tuple(map(int, input().split()))
string = input()
print(solution(a,b,string))