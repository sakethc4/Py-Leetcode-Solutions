# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # O(N) Time & O(1) Space. 
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True 
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, leftNode, rightNode):
        if leftNode is None and rightNode is None:
            return True 
        if leftNode is None or rightNode is None:
            return False
        return leftNode.val == rightNode.val and self.isMirror(leftNode.left, rightNode.right) and self.isMirror(leftNode.right, rightNode.left)
