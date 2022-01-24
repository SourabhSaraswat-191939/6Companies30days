# Pots of Gold Game (Similar to Covid and Beds problem)

# The idea is to find an optimal strategy that makes player A win knowing that player B is playing optimally as well.
# The player has 2 choices for the coin[i....j] where i and j represent front and rear of the line respectively.
# CASE 1:
# If player A chooses from pot i, player B is left to choose from [i+1 to j]
#     1. If player B chooses from pot i + 1, recurse for [i + 2...j]
#     2. If player B chooses from pot j, recurse for [i + 1...j - 1]
# CASE 2:
# If player B chooses from pot j, player B is left to choose from [i to j - 1]
#     1. If player B chooses from pot i, recurse for [i + 1...j - 1]
#     2. If player B chooses from pot j - 1, recurse for [i...j - 2]


# Time Complexity -> n^2 and Space Complexity -> (n^2)/2

def maxCoins(arr, n):
    dp = {}
    
    def optimalMove(i,j):
        if i==j:
            return arr[i]
        if i+1==j:
            return max(arr[i],arr[j])
        
        if (i,j) in dp:
            return dp[(i,j)]
        
        selectStart = arr[i] + min(optimalMove(i+2,j),optimalMove(i+1,j-1))
        selectEnd = arr[j] + min(optimalMove(i+1,j-1),optimalMove(i,j-2))
        dp[(i,j)] = max(selectStart,selectEnd)
        return dp[(i,j)]
    
    return optimalMove(0,n-1)

print(maxCoins([8, 15, 3, 7],4))