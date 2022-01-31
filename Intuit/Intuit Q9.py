# https://leetcode.com/problems/pacific-atlantic-water-flow/

def pacificAtlantic(heights):
    if not heights:
        return []
    
    p_visited = set()
    a_visited = set()
    xDir = [1,-1,0,0]
    yDir = [0,0,1,-1]
    
    def dfs(i,j,visited):
        if (i,j) in visited:
            return
        visited.add((i,j))
        for ind in range(4):
            x,y = i+xDir[ind], j+yDir[ind]
            if x<0 or y<0 or x>=len(heights) or y>=len(heights[0]) or heights[x][y]<heights[i][j]:
                continue
            dfs(x,y,visited)
    
    for i in range(len(heights)):
        # p_visited[i][0] = True
        # a_visited[i][n-1] = True
        dfs(i,0, p_visited)
        dfs(i,len(heights[0])-1, a_visited)
    
    for j in range(len(heights[0])):
        # p_visited[i][0] = True
        # a_visited[i][n-1] = True
        dfs(0,j, p_visited)
        dfs(len(heights)-1,j, a_visited)
    
    return list(p_visited & a_visited)   # doing & operation to know points which can visit both oceans.

# print(pacificAtlantic([[10,10,10],[10,1,10],[10,10,10]]))
print(pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,0,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
# print(pacificAtlantic([[2,1],[1,2]]))
