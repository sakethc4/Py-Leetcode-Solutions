# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # O(N) Time & O(N) Space. 
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inOrderAux(root, result)
        return result 
    
    def inOrderAux(self, root, result):
        if root is None:
            return
        self.inOrderAux(root.left, result)
        result.append(root.val)
        self.inOrderAux(root.right, result)
    
     