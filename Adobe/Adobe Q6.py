# Generate Parentheses

# Time Complexity-> O(2^N * N); Space Complexity: O(2*N*X), X = Number of valid Parenthesis.

def AllParenthesis(n):
    result = []
    def generate(cOpen,cClose,s):
        if cOpen+cClose==2*n:
            result.append(s)
            return
        
        if cOpen==cClose:
            generate(cOpen+1,cClose,s+'(')
        else:
            if cOpen<n:
                generate(cOpen+1,cClose,s+'(')
            generate(cOpen,cClose+1,s+')')
    
    generate(0,0,'')
    return result

print(AllParenthesis(3))