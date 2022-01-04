# Decode the string


# Approach 1 using 2 Stacks
def decodedString(s):
    stackChar = []
    stackNums = []
    nums = set([str(x) for x in range(0,10)])
    num = ''
    for i in range(len(s)):
        if s[i] in nums:
            if num != '':
                num = stackNums.pop() + s[i]
                print(num)

            else:
                num = s[i]
            stackNums.append(num)
            continue
        if s[i]==']':
            multiply = stackNums.pop()
            out = ''
            while True:
                poped = stackChar.pop()
                if poped=='[':
                    break
                out = poped+out
            if len(stackChar)==0:
                return int(multiply)*out
            stackChar.append(int(multiply)*out)
        
        else:
            num =''
            stackChar.append(s[i])
    return ""




# Approach 2 Using 1 Stack
def decodedString2(s):
    stack = []
    currString = ''
    currNum = 0
    
    for c in s:
        if c=='[':
            stack.append(currString)
            stack.append(currNum)
            currString = ''
            currNum = 0
            
        elif c==']':
            num = stack.pop()
            currString = stack.pop() + num*currString
            
        elif c.isdigit():
            currNum = currNum*10+int(c)
        else:
            currString += c
    
    return currString

print(decodedString('3[b12[ca]]'))