# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # O(N) Time & O(N) Space. 
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(currNode, lower=float("-inf"), upper=float("inf")):
            if currNode is None:
                return True 
            if not (lower < currNode.val < upper):
                return False 
            
            return dfs(currNode.left, lower, currNode.val) and dfs(currNode.right, currNode.val, upper)
        return dfs(root)