# Minimum Size Subarray Sum

# Time Complexity -> O(n)
def minSubArrayLen(target, nums):
    i=0
    result = 0
    length = len(nums)+1
    for j in range(len(nums)):
        result += nums[j]
        while result>=target:
                if length > j-i+1:
                    length = j-i+1
                    if length==1:
                        return 1
                result -= nums[i]
                i+=1
    
    return length if length!=len(nums)+1 else 0

print(minSubArrayLen(7,[2,3,1,2,4,3]))

