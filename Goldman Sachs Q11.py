# Given an unsorted array Arr of size N of positive integers. One number 'A' from     set {1, 2, …N} is missing and one number 'B' occurs twice in array. Find these two numbers.

def findTwoElement(arr, n): 
    visited = set()
    B= None
    arrSum = 0
    for num in arr:
        if B is None:
            if num in visited:
                B=num
            visited.add(num)
        arrSum += num
    
    realSum = 0
    for x in range(1,n+1):
        realSum += x 
    # diff = arrSum - realSum
    print(B, arrSum, realSum)
    A = B-arrSum + realSum
    return [B,A]

print(findTwoElement([1,3,3,4,5],5))