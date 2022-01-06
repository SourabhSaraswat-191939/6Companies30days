# Given two strings str1 and str2. We say that str2 divides str1 if it's possible to concatenate multiple str2 to get str1. For example, ab divides abab. if str2 does not divide str1, return -1. Otherwise, return the smallest string str3 such that str3 divides both str1 and str2.

def gcdOfStrings(self, str1: str, str2: str) -> str:
    l1 = len(str1)
    l2 = len(str2)
    if l1>l2:
        temp = str1
        str1 = str2
        str2 = temp
        
    ans = str1
    
    while True:
        check2 = False
        check1 = False
        if ans=="":
            return ""
        for i in range(1,1 + len(str2)//len(ans)):
            if ans*i==str1:
                check1 = True
                
            if ans*i==str2:
                check2 = True
                break
                
        if check2 and check1:
            break
            
        ans = ans[:len(ans)-1]
    
    return ans