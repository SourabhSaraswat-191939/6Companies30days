# String Amendment

def amendSentence(s):
    i=0
    result = ''
    for ch in s:
        asci = ord(ch)
        if asci>=65 and asci<=90:
            result += ' '+str(chr(asci-65+ 97))
        else:
            result+= ch
        
    return result.strip()

print(amendSentence('dXfiRCVS'))