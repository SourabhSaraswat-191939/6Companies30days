# Given a string, Your task is to  complete the function encode that returns the run length encoded string for the given string. eg if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3d1e1x6″

def encode(arr):
    ans = arr[0]
    prev = arr[0]
    count = 0
    for c in arr:
        if c==prev:
            count+=1
        else:
            ans += str(count)
            ans += c
            count = 1
        prev = c
    ans += str(count)
    return ans

print(encode("aaaabbbccc"))