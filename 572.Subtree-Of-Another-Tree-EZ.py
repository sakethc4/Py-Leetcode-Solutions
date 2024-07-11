# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # O(N) Time & O(N) Space. 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None: 
            return True
        if root is None:
            return False 
        if self.same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 

    def same(self, root, subRoot):
        if root is None and subRoot is None: 
            return True
        if root and subRoot and root.val == subRoot.val:
            leftTree = self.same(root.left, subRoot.left)
            rightTree = self.same(root.right, subRoot.right)
            return leftTree and rightTree
        return False   

         