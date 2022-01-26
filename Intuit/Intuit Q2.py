# Word Search

def isWordExist(board, word):
    start = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if word[0]==board[i][j]:
                start.append((i,j))
                
    rows = [0,0,-1,1]
    cols = [1,-1,0,0]
    
    def findWord(i,j,index):
        if index>=len(word):
            # print("check",index)
            return True
        if i>=len(board) or j>=len(board[0]) or i<0 or j<0:
            return False
        if word[index]!=board[i][j]:
            return False
        
        # print("Working",index,word[index])
        
        board[i][j] = '$'
        for rc in range(4):
            if findWord(i+rows[rc],j+cols[rc],index+1):
                return True
        board[i][j] = word[index]
        return False
    
    for i,j in start:
        if findWord(i,j,0):
            return True
            
    return False

print(isWordExist([['a','g','b','c'],['q','e','e','l'],['g','b','k','s']],word = "geeks"))


# 3 4
# a b c e
# s f c s
# a d e e
# sabfs