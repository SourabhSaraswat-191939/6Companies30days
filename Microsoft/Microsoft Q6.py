# Possible Words From Phone Digits

def possibleWords(a,N):
    alpha = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    result = []
    def listing(count,temp):
        if count==N:
            result.append(temp)
            return

        for c in alpha[a[count]]:
            temp += c
            listing(count+1,temp)
            temp = temp[:-1]
    
    for c in alpha[a[0]]:
        listing(1,c)    

    return result

print(possibleWords([2,3,4],3))