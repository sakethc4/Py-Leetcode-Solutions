# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: # O(N) Time & O(N) Space. 
    def removeNodes(self, head):
        # Use a monotonic stack (that is increasing). 
        stack = [] 
        current = head
        while current:  
            while stack and stack[-1].val < current.val: 
                stack.pop() 
            if stack: 
                stack[-1].next = current 
            stack.append(current)
            current = current.next 
        return stack[0] if stack else None 
