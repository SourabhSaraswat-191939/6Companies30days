# Given a matrix of size r*c. Traverse the matrix in spiral form. 


# Approach 1,  Time Complexity: O(r*c),  Space Complexity: O(r*c)
def spirallyTraverse(matrix, r, c):
    ans = []
    if len(matrix)==0:
        return ans
    seen = [[0 for i in range(c)] for j in range(r)]
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    R = 0
    C = 0
    di = 0
    for i in range(r*c):
        ans.append(matrix[R][C])
        seen[R][C] = True
        cr = R+dr[di]
        cc = C+dc[di]
        if 0<=cr and cr<r and 0<=cc and cc<c and not(seen[cr][cc]):
            R = cr
            C = cc
        else:
            di = (di+1)%4
            R += dr[di]
            C += dc[di]
    return ans

# Approach 2,  Time Complexity: O(r*c),  Space Complexity: O(1)
def spirallyTraverse2(a,m,n):   #(array,row,col)
    k = 0
    l = 0
    ''' k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator '''
    ans = []
    while (k < m and l < n):
        # Print the first row from
        # the remaining rows
        for i in range(l, n):
            ans.append(a[k][i])

        k += 1

        # Print the last column from
        # the remaining columns
        for i in range(k, m):
            ans.append(a[i][n - 1])

        n -= 1

        # Print the last row from
        # the remaining rows
        if (k < m):
            for i in range(n - 1, (l - 1), -1):
                ans.append(a[m - 1][i])

            m -= 1

        # Print the first column from
        # the remaining columns
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                ans.append(a[i][l])

            l += 1
    return ans

print(spirallyTraverse([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15,16]],4,4))
print(spirallyTraverse2([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15,16]],4,4))