# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: # O(N) Time & O(1) Space. 
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current, previous = head.next, head.next 
        # Track sum. 
        sum = 0
        while current:
            value = current.val 
            # Case 1: Numeric value. We need to add this node.val to our sum.
            if value != 0: 
                sum += value
            # Case 2: We hit a zero we need to take the sum value and make it
            # an "official node".
            else: 
                previous.val = sum
                previous.next = current.next
                previous = previous.next
                sum = 0    
            current = current.next
        return head.next  