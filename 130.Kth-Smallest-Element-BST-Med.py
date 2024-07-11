# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # O(N) Time & O(N) Space. 
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [] 
        currNode = root 
        while stack or currNode:
            while currNode:
                stack.append(currNode)
                currNode = currNode.left
            currNode = stack.pop()
            k -= 1
            if k == 0:
                return currNode.val
            currNode = currNode.right