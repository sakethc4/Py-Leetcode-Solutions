# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.count = 0 
        def dfs(currNode):
            if currNode is None: 
                return []
            if currNode.left is None and currNode.right is None:
                return [1]
            
            leftDist = dfs(currNode.left)
            rightDist = dfs(currNode.right)
            # Calculating total dist. 
            for l in leftDist:
                for r in rightDist:
                    if l + r <= distance: 
                        self.count += 1
            return [dist + 1 for dist in leftDist + rightDist if dist + 1 <= distance] 
        dfs(root)
        return self.count