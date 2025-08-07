def solution(n):
    dp = [0] *(n+1)
    dp[0] = 1
    
    for i in range(1, n+1):
        for k in range(i):
            dp[i] += dp[k] * dp[i-1-k]
    return dp[n]