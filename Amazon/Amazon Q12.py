# Column name from a given column number

def colName (self, n):
    result = ''
    while True:
        if n<27:
            result=chr(64+n)+result
            break
        if n%26==0:
            result = 'Z'+result
            n-=1
        else:
            result = chr(64+n%26)+result
        n = n-(n%26)
        n//=26
        
    return result
    
print(colName(470211273))