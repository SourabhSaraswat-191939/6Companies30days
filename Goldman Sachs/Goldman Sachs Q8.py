# Total Decoding Messages

# using Bottom Up Approach DP
def CountWays(str):
    mod = 1e9 + 7
    n = len(str)
    if str[0]=='0':
        return 0
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2,n+1):
        if str[i-1]>'0':
            dp[i] = dp[i-1]
        
        if str[i-2]=='1' or (str[i-2]=='2' and str[i-1]<'7'):
            dp[i] += dp[i-2]
    
    return int(dp[n]%mod)


print(CountWays('123'))


# using Top Down Approach DP (Some errors in my code, I have to solve that.)
# def CountWays(self, str):
#     if str=="":
#         return 1
#     if str[0]=="0":
#         return 0 
#     mod = 1e9 + 7
#     dp = {}
#     def countComb(s,dp,index):
#         if index in dp:
#             return dp[index]
        
#         if s=="":
#             return 1
#         if s[-1]=="0":
#             return 0
#         if len(s)<2:
#             return 1
#         if s[0]=="0":
#             return 1
            
#         if int(s[:2])>26:
#             dp[index] = countComb(s[1:],dp,index+1)
#             return dp[index]
            
#         dp[index] = countComb(s[1:],dp,index+1)+countComb(s[2:],dp,index+2)
#         return dp[index]
        
#     return int(countComb(str,dp,0)%mod)