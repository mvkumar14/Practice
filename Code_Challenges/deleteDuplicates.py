class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        if not self.next:
            return str(self.val)
        return str(self.val) + " " + str(self.next)

class Solution(object):
    def delete_duplicates(self, node):
        # keep values in a cache
        # if next.value is a duplicate value (in cache)
        # then set self.next to next.next and check 
        # again
        # if its a new value
        # add it to the cache and "focus" next
        cache = []
        cache.append(node.val)
        current = node  # is this better form or is it better form
        # to do node.next and modify node which was the input value?
        while current.next is not None:
            if current.next.val in cache:
                current.next = current.next.next  # assuming garbage collection?
                current = current.next
            else: 
                cache.append(current.next.val)
                current = current.next

# The way the problem is phrased it seems like you need to mutate an object
# instead of returning a new one

# Why does the Solution class inherit from "object" What is the "object" class?
# when would I inherit from the "object" class

n = Node(1, Node(3, Node(3, Node(4))))
print(n)
Solution().delete_duplicates(n)
print(n)      