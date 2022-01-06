# Rotten Oranges -Multiple Repetitions

def orangesRotting(grid):
    rotenIndex = []
    time = []
    for i in range(len(grid)):
        row = []
        for j in range(len(grid[0])):
            row.append(0)
            if grid[i][j]==2:
                rotenIndex.append((i,j))
        time.append(row)
        
    def dfs(i,j,visited,count):
        if i>=len(time) or j>=len(time[0]) or i<0 or j<0:
            return
        
        if grid[i][j]==0:
            return
        if (i,j) in visited:
            if time[i][j]<count:
                return 
        
        visited.add((i,j))
        time[i][j] = count
        grid[i][j]= 2
        xDir = [0,1,-1,0]
        yDir = [1,0,0,-1]
        for k in range(4):
            dfs(i+xDir[k],j+yDir[k],visited,count+1)

    visited = set()
    for i,j in rotenIndex:
        dfs(i,j,visited,0)
    
    maxTime = 0
    for i in range(len(time)):
        for j in range(len(time[0])):
            if grid[i][j]==1:
                return -1
            if maxTime<time[i][j]:
                maxTime = time[i][j]
        
    return maxTime

print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))