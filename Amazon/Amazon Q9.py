# Which among them forms a perfect Sudoku Pattern ?

def isValid(self, mat):
        # code here
        def check(r,c):
            for i in range(len(mat)):
                if i!=r and mat[i][c]==mat[r][c]:
                    return False
            
            for j in range(len(mat[0])):
                if j!=c and mat[r][j]==mat[r][c]:
                    return False
                    
            ri = 3*(r//3)
            ci = 3*(c//3)
            for i in range(ri,ri+3):
                for j in range(ci,ci+3):
                    if i!=r and j!=c and mat[i][j]==mat[r][c]:
                        return False        
            return True
            
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col]!=0:
                    if not check(row,col):
                        return 0
                        
        return 1