# Implement Atoi

def atoi(string):        
    result = 0
    start=0
    sign = 1
    if string[0]=='-':
        start=1
        sign = -1
        
    for i in range(start,len(string)):
        if string[i]==' ':
            break
        val = ord(string[i])-ord('0')
        if val<=9 and val>=0:
            result = result*(10)+val
            
        else:
            return -1
            
    return result*sign
    
print(atoi('-123'))