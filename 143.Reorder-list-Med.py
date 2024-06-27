# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: # O(N) & O(1) Space. 
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: 
            return 
        # First we can find the middle of our LinkedList.
        slow, fast = head, head
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next
        # Now reverse the second half of our input list. 
        current, previous = slow, None 
        while current: 
            nxt = current.next
            current.next = previous 
            previous = current 
            current = nxt
        # Now we can merge. 
        first, second = head, previous 
        while second.next: 
            temporaryOne, temporaryTwo = first.next, second.next 
            first.next = second 
            second.next = temporaryOne 
            first, second = temporaryOne, temporaryTwo 
               
        