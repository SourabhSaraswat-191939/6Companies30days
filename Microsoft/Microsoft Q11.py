from queue import Queue
def generate(n):
    N = n
    ans = []
    q = Queue()
    q.put("1")
    ans.append("1")
    while n>0:
        n-=1
        s1 = q.get()
        
        s2 = s1
        q.put(s1+"0")
        ans.append(s1+"0")
        q.put(s2+"1")
        ans.append(s2+"1")
    
    print(n)
    return ans[:N]

print(generate(2))