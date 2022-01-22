# Partition Equal Subset Sum

# Approach 1 => Using Top Down
def equalPartition(N, arr):
    target = 0
    for i in range(N):
        target+=arr[i]
    if target%2==1:
        return 0
    target = target//2
    dp = []

    # Approach 1 => Using Top Down
    # for i in range(N+1):
        #     temp = []
        #     for j in range(target+1):
        #         temp.append(-1)
        #     dp.append(temp)
                
    # def findSubsetSum(i,w):
    #     if w==0:
    #          return True
    #     if i==0:
    #         return False
    #     if dp[i][w]!=-1:
    #         return dp[i][w]
    #     if arr[i-1]<=w:
    #         dp[i][w] = (findSubsetSum(i-1,w-arr[i-1]) or findSubsetSum(i-1,w))
    #     else:
    #         dp[i][w] = findSubsetSum(i-1,w)
    #     return dp[i][w]
        
    # return 1 if findSubsetSum(N,target) else 0
    
    
    # Approach 2 => Using Bottom Up
    for i in range(N+1):
        temp = []
        for j in range(target+1):
            temp.append(False)
            
        dp.append(temp)
    dp[0][0] = True
    for i in range(1,N+1):
        for j in range(1,target+1):    
            if arr[i-1]<=j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
            
    return 1 if dp[N][target] else 0

print(equalPartition(3,[1, 3, 5]))