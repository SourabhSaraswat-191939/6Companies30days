# Find the length of the Longest Arithmetic Progression (LLAP) in it.

def lengthOfLongestAP(A, n):
    dp = [{} for _ in range(n)]
    maxCount = 0
    for i in range(1,n):
        for j in range(i):
            diff = A[i]-A[j]
            if diff in dp[j]:
                dp[i][diff] = dp[j][diff]+1
            else:
                dp[i][diff] = 1
            
            if dp[i][diff]>maxCount:
                maxCount = dp[i][diff]
    
    return maxCount+1

print(lengthOfLongestAP([1, 7, 10, 13, 14, 19],6))