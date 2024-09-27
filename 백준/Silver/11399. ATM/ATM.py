def solution(n,p):
#p를 오름차순으로 배열해서 합합
    p = sorted(p)
    answer = 0
    for i in range(n):
        for m in range(i+1):
            answer += p[m]
    return answer
#a,b = tuple(map(int, input().split()))
n = int(input())
p = list(map(int, input().split()))
print(solution(n,p))