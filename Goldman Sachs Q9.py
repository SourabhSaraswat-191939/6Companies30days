# Given a pattern containing only I's and D's. I for increasing and D for decreasing.Devise an algorithm to print the minimum number following that pattern.


def findMinNumberPattern(Str):
    ans = "" 
    i = 0
    cur = 1 
    dCount = 0 
    while (i < len(Str)) :
        ch = Str[i]
        if (i == 0 and ch == 'I') :
            ans += str(cur)
            cur+=1
        if (ch == 'D') :
            dCount+=1
            
        j = i + 1
        while (j < len(Str) and Str[j] == 'D') :
            dCount+=1
            j+=1
         
        k = dCount
        while (dCount >= 0) :
            ans += str(cur + dCount)
            dCount-=1
         
        cur += (k + 1)
        dCount = 0
        i = j
 
    return ans