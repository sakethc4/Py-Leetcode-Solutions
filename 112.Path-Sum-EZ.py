# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # O(N) Time & O(N) Space. 
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(currNode, sum):
            if currNode is None:
                return False 
            
            sum += currNode.val
            if currNode.left is None and currNode.right is None:
                return sum == targetSum
            return (dfs(currNode.left, sum) or dfs(currNode.right, sum))
        return dfs(root, 0) 