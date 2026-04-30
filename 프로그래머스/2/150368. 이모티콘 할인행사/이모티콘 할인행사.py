from itertools import product

def solution(users, emoticons):
    answer = []
    discount = [10, 20, 30, 40]
    n = len(emoticons)
    
    for p in product(discount, repeat = n):
        count = 0
        sum_price = 0
        
        for u_ratio, u_price in users:
            user_sum = 0
            didBuy = False
            for m in range(len(p)):
                if p[m] >= u_ratio:
                    user_sum += emoticons[m]*((100-p[m])/100)
                if user_sum >= u_price:
                    count += 1
                    didBuy = True
                    break
            # 만약 전환 안됐다면, 구매한 금액 추가
            if not didBuy:
                sum_price += user_sum
        
        answer.append((count, sum_price))
            
    return sorted(answer, reverse = True)[0]