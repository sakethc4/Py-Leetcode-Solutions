# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: # O(N) Time & O(1) Space. 
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroup = dummy 
        # Checking how many nodes to reverse. 
        while True: 
            kth = self.getGroup(prevGroup, k)
            if not kth: 
                break 
            nextGroup = kth.next 
            # Now do reversal. 
            current, previous = prevGroup.next, kth.next
            while current != nextGroup:
                tmp = current.next
                current.next = previous
                previous = current
                current = tmp

            tmp = prevGroup.next
            prevGroup.next = kth
            prevGroup = tmp
        return dummy.next

    def getGroup(self, current, k):
        while current and k > 0:
            current = current.next
            k -= 1
        return current 


         