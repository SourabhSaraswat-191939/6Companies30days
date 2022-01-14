from re import L


def rotate(matrix): 
    #code here
    n = len(matrix)
    for i in range(n):
        point = matrix[i][i]
        for j in range(i+1,n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(n//2):
        matrix[i],matrix[-i-1] = matrix[-i-1],matrix[i]

    return matrix

# print(rotate)

if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		N=int(input())
		arr=[int(x) for x in input().split()]
		matrix=[]

		for i in range(0,N*N,N):
			matrix.append(arr[i:i+N])

		rotate(matrix)
		for i in range(N): 
			for j in range(N): 
				print(matrix[i][j], end =' ') 
			print() 
        

# } Driver Code Ends