'''
Time Complexity: O(n)
Space Complexity: O(n)
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if(not root): return root
        q = deque([])
        q.append(root)
        while(len(q)>0):
            temp = deque([])
            prev = None
            while(len(q)>0):
                val = q.popleft()
                if(prev):
                    prev.next = val
                if(val.left and val.right):
                    temp.append(val.left)
                    temp.append(val.right)
                prev = val
            prev.next = None
            q = temp
        return root
                    
            
        