# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: # O(N) Time & O(1) Space.
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr:
            nxt = curr.next # node after curr 
            curr.next = prev # next pointer is prev
            prev = curr # makes curr new prev 
            curr = nxt # moves us to next node 
        return prev
