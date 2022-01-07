# Delete N nodes after M nodes of a linked list

def skipMdeleteN(self, head, M, N):
    if N==0:
        return head
    ptr = head
    skip = M
    delete = N

    while (ptr is not None):
        while (ptr.next != None) and M>1:
            ptr = ptr.next
            M-=1
        
        if ptr is None:
            return head
        
        start = ptr
        ptr = ptr.next
        while (ptr is not None) and N>1:
            ptr = ptr.next
            N-=1
        
        if ptr is None:
            start.next = None
            return head
        
        start.next = ptr.next
        ptr.next = None
        ptr = start.next
        M= skip
        N= delete
        
    return head