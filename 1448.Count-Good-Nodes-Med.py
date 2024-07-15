# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # O(N) Time & O(N) Space. 
    def goodNodes(self, root: TreeNode) -> int:
        count = 0 
        def dfs(currNode, biggest): 
            nonlocal count
            if currNode is None:
                return 0 
            if currNode.val >= biggest:
                count += 1 
            biggest = max(biggest, currNode.val)
            dfs(currNode.left, biggest)
            dfs(currNode.right, biggest)
        dfs(root, root.val)
        return count 

