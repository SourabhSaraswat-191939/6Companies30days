# Brackets in Matrix Chain Multiplication 

def matrixChainOrder(p, n):
    m = [[0 for _ in range(n)] for i in range(n)]
    
    # place parenthesis at different places
    # between first and last matrix,
    # recursively calculate count of
    # multiplications for each parenthesis
    # placement and return the minimum count
    # d is chain length 
    for l in range (2, n + 1):
        for i in range (n - l + 1):
            j = i + l - 1
 
            # Initializing infinity value.
            m[i][j] = float('Inf')
            for k in range (i, j):
                q = (m[i][k] + m[k + 1][j] +(p[i] * p[k + 1] * p[j + 1]))
                if (q < m[i][j]):
                    m[i][j] = q
 
                    # Storing k value in opposite index.
                    m[j][i] = k + 1
    
    global result
    result = ""
    def printParenthesis(j, i):
        # Displaying the parenthesis.
        global result
        if j == i:
            # The first matrix is printed as
            # 'A', next as 'B', and so on
            result +=chr(65 + j)
            return
        else:
            result +="("
    
            # Passing (m, k, i) instead of (s, i, k)
            printParenthesis(m[j][i] - 1, i)
    
            # (m, j, k+1) instead of (s, k+1, j)
            printParenthesis(j, m[j][i])
            result +=")"
    for row in m:
        print(row)
    printParenthesis(n - 1, 0)
    return result


arr = [1, 2, 3, 4, 5]
n = len(arr) - 1
 
print(matrixChainOrder(arr, n))