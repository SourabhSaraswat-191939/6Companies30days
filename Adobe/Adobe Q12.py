# Leaders in Array 

def leaders(A, N):
    maxi = -1
    result = []
    for i in range(N-1,-1,-1):
        if A[i]>=maxi:
            result.append(A[i])
            maxi = A[i]
        
    result.reverse()
    return result

print(leaders([1,2,3,4,0],5))