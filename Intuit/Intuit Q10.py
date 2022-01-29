# https://leetcode.com/problems/number-of-provinces/

def findCircleNum(isConnected):
    result = 0
    visited = set()
    
    def dfs(src, visited):
        if src in visited:
            return
        visited.add(src)
        for i in range(len(isConnected)):
            if (i not in visited) and isConnected[src][i]==1:     
                dfs(i,visited)
        
    
    for i in range(len(isConnected)):
        if i not in visited:
            dfs(i,visited)
            result +=1
    return result

print(findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))