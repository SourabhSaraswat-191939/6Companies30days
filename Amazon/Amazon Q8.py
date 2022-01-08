# Count ways to N'th Stair(Order does not matter)

# Approach 1, using the general DP way.
def countWays(m):        
    mod = 1000000007
    dp = [0]*(m+1)
    dp[0] = 1
    
    for step in [1,2]:
        for i in range(m+1):
            if step>i:
                continue
            dp[i] = dp[i]+dp[i-step]
            
    return dp[m]%mod
    
# Approach 2=> Got this approach by analysing the dp resultant array of Approach 1.
def countWays2(m):        
    return ((m-(m)%2)//2)+1
    

print(countWays(5))
print(countWays2(5))