# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # O(N) Time & O(N) Space.
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Validate the root. 
        if not root:
            return
        queue = deque()
        queue.append(root)
        while queue:
            currNode = queue.popleft()
            currNode.left, currNode.right = currNode.right, currNode.left
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)
        return root 