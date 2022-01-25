# Minimum operations to convert array A to B 

def minInsAndDel(A, B, m, n):
    def lcs(X , Y):
        L = [[None]*(n+1) for i in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0 :
                    L[i][j] = 0
                elif X[i-1] == Y[j-1]:
                    L[i][j] = L[i-1][j-1]+1
                else:
                    L[i][j] = max(L[i-1][j] , L[i][j-1])
        
        # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
        return L[m][n]
    
    LCS = lcs(A,B)
    return (m-LCS)+(n-LCS)

print(minInsAndDel([1, 2, 5, 3, 1],[1, 3, 5],5,3))