def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1
    mod = 1_000_000_007
    
    for coin in money:
        for i in range(coin, n + 1):
            dp[i] = (dp[i] + dp[i - coin]) % mod
            
    return dp[n]
