# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # O(N) Time & O(N) Space. 
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float("-inf")
        def dfs(currNode):
            nonlocal maxSum 
            if currNode is None:
                return 0 
            leftTree = max(0, dfs(currNode.left))
            rightTree = max(0, dfs(currNode.right))
            currSum = leftTree + rightTree + currNode.val
            maxSum = max(maxSum, currSum)
            return currNode.val + max(leftTree, rightTree)
        dfs(root)
        return maxSum 