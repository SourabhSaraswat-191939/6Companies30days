# Approach 1, TC -> O(n), SC -> O(n)
def FindMaxSum(a, n):
        inc = a[0]
        exc = 0
        i=1
        while i<n:
            exc_new = inc if inc>exc else exc
            inc = exc+a[i]
            exc = exc_new
            i+=1
        return max(inc,exc)

# Approach 2, TC -> O(n), SC -> O(1)
def FindMaxSum2(a, n):
    dp = [0]*n
    def findMax(i,dp):
        if i>=n:
            return 0
        if dp[i]!=0:
            return dp[i]
        dp[i] = max(findMax(i+2,dp)+a[i],findMax(i+3,dp)+a[i])
        return dp[i]
    
    return max(findMax(0,dp),findMax(1,dp))

print(FindMaxSum([9,8,3,8,5],5))
print(FindMaxSum2([9,8,3,8,5],5))