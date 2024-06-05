class Solution: # O(N) Time and O(1) Space 
    def findMiddle(self, head):
        # We are given the head and we want to return the middle not of the LinkedList. 
        # Example: 1 => 2 => 3 => 4 => => 5 => 6 => null 
        # Two pointers one fast and one slow (slow can move 1 at a time), (fast can move 2 at a time). 
        slow, fast = head, head 
        # Iterate till our fast pointer reaches a null node (i.e end of list)
        while(fast is not None and fast.next is not None):
            fast = fast.next.next
            slow = slow.next
        # return the slow pointer which would be the location of the middle of the LinkedList. 
        return slow 
            



