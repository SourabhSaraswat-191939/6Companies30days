# Connect Nodes at Same Level

from queue import Queue
def connect(self, root):
    queue = Queue()
    ptr = root
    queue.put(ptr)
    queue.put(None)
    prev = None
    while not queue.empty():
        out = queue.get()
        # if out == None:
        #     if prev is not None:
        #         prev.nextRight = None
        #     continue
        if out is not None:
            # if prev is None:
            #     prev = out
            #     continue
            out.nextRight = queue.queue[0]
            prev = out
            if out.left:
                queue.put(out.left)
            if out.right:
                queue.put(out.right)
        elif not queue.empty():
            queue.put(None)
    # prev.nextRight = None
    return root
