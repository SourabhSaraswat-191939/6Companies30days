from operator import mod

# Approach 1=> With Recursion (Chances of exceeding recursion dept in some cases)
def numOfWays(n, x):    
    dp = {}
    def find(n,x,num):
        val = n-(num**x)
        if val==0:
            return 1
        if val<0:
            return 0
            
        if (n,num) in dp:
            return dp[(n,num)]
        dp[(n,num)] = find(val,x, num+1) + find(n,x, num+1)
        return dp[(n,num)]
    
    return int((find(n,x,1))%(1e9+7))

# Approach 2=> With iteration
def numOfWays2(n, power):        
    mod = 1e9 + 7
    dp = [0]*(n+1)
    dp[0] = dp[1] = 1 
    for powerOf in range(2,n+1):
        for numberToMake in range(n,powerOf-1,-1):
            y = powerOf**power
            if y<=numberToMake:
                dp[numberToMake] = int((dp[numberToMake]+dp[numberToMake-y])%mod)
    return dp[n]


print(numOfWays2(1000,1))
print(numOfWays(1000,1))