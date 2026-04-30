from itertools import permutations

def solution(expression):
    answer = 0
    op = ["+", "-", "*"]
    
    numbers = []
    my_op = []
    
    # 숫자와 연산자 분리해서 순서대로 받기
    last_op_idx = -1
    for i in range(len(expression)):
        if expression[i] in op:
            # last_op_idx+1 ~ i-1까지 숫자 추가
            numbers.append(int(expression[last_op_idx+1:i]))
            my_op.append(expression[i])
            last_op_idx = i
    # 마지막 숫자 추가
    numbers.append(int(expression[last_op_idx+1:]))
            
    # 연산자 우선순위 정하기
    for p in permutations(op):
        # 연산자 우선순위 바뀌면 원래 nums, my_op로 초기화
        nums = numbers[:]
        ops = my_op[:]
        
        for cur_op in p:
            while cur_op in ops:
                idx = ops.index(cur_op)
                
                if cur_op == "+":
                    cal = nums[idx] + nums[idx+1] 
                elif cur_op == "-":
                    cal = nums[idx] - nums[idx+1]
                else:
                    cal = nums[idx] * nums[idx+1]
                    
                ops.pop(idx)
                nums.pop(idx+1)
                nums[idx] = cal
                
        answer = max(answer, abs(nums[0]))
    
    return answer