# Unit Area of largest region of 1's

def findMaxArea(grid):
    r = len(grid)
    c = len(grid[0])

    visited = set()
    dirX = [0,1,1,1,0,-1,-1,-1]
    dirY = [1,0,1,-1,-1,-1,0,1]
    
    def dfs(row,col):
        if row<0 or col<0 or row>=r or col>=c or grid[row][col]==0:
            # print("break",row,col)
            return 0
        count = 1
        visited.add((row,col))
        for i in range(8):
            if (row+dirX[i],col+dirY[i]) in visited:
                continue
            count +=dfs(row+dirX[i], col+dirY[i])
        return count

    maxCount = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]!=1 or (row,col) in visited:
                continue
            count = dfs(row,col)
            if count>maxCount:
                maxCount = count

    return maxCount

# print(findMaxArea([[1,0],[0,1]]))
print(findMaxArea([[1,1,1,0],[0,0,0,1],[1,1,0,1]]))