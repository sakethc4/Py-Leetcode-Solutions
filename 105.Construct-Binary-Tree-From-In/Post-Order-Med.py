# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# We can use the index of preorder[0] to find how many nodes
# on left in preorder tree 
class Solution: # O(N) Time & O(N) Space.
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # Find root node. 
        root = TreeNode(preorder[0])
        remainder = inorder.index(preorder[0])
        # Build the tree.
        root.left = self.buildTree(preorder[1 : remainder + 1], inorder[: remainder])
        root.right = self.buildTree(preorder[remainder + 1 :], inorder[remainder + 1:])
        return root