# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # O(N) Time & O(N) Space. 
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result = float("inf")
        prevNode = None 
        def dfs(currNode):
            nonlocal result, prevNode 
            if currNode is None:
                return 
            dfs(currNode.left)
            if prevNode:
                result = min(result, currNode.val - prevNode.val)
            prevNode = currNode 
            dfs(currNode.right)
        dfs(root)
        return result 