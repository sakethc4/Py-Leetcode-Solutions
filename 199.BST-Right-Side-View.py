# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # O(N) TIme & O(N) Space. 
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = [] 
        if root is None: 
            return root 
        queue = deque()
        queue.append(root)
        while queue: 
            currLvl = deque()
            lvlSize = len(queue)
            for _ in range(lvlSize):
                currNode = queue.popleft() 
                currLvl.appendleft(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            result.append(currLvl[0])
        return result 