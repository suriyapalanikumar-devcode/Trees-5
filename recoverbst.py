'''
Time Complexity: O(n)
Space Complexity: O(h)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        op = []
        prev = [None]
        def inorder(root):
            if(not root):
                return None
            inorder(root.left)
            if(prev[0] and prev[0].val>root.val):
                if(len(op)==0):
                    op.append(prev[0])
                    op.append(root)
                else:
                    op[1] = root
            prev.pop()
            prev.append(root)
            inorder(root.right)
            
        inorder(root)
        temp = op[0].val
        op[0].val = op[1].val
        op[1].val = temp
        
        
                
            
            