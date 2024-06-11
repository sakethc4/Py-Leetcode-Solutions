class Solution: # O(N) Time and O(1) Space 
    def reorder(self, head): 
        # Singly LL. Modify so that the nodes in the second half are inserted 
        # alternately to the nodes in the first half in reverse order. 
        # INPUT: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null . 
        # OUTPUT: 2 -> 12 -> 4 -> 6 -> 10 -> 8 -> null. 
        # Checking to ensure head is valid. 
        if head is None or head.next is None: 
            return head 
        # Go through out input list. We can find the middle value.
        # Initialize two pointers.
        slow, fast = head, head 
        # Iterate through Linked List. 
        while fast is not None and fast.next is not None: 
            # Move slow by 1. 
            slow = slow.next
            # Move fast by 2. 
            fast = fast.next.next 
        # We can set that to head for the second half of the list. We can go thru and reverse the second half. 
        headSecondHalf = self.reverse(slow)
        headFirstHalf = head 
        # Go through the LL from beginning and insert as needed. 
        # INPUT: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null. 
        # Output: 2 -> 12 -> 4 -> 10 -> 4 -> 8 -> null. 
        while headFirstHalf is not None and headSecondHalf is not None: 
            # temp variable to store next element for first half 
            tempFirstHalf = headFirstHalf.next 
            headFirstHalf.next = headSecondHalf 
            headFirstHalf = tempFirstHalf
            # temp variable to store next element for second half. 
            tempSecondHalf = headSecondHalf.next 
            headSecondHalf.next = headFirstHalf
            headSecondHalf = tempSecondHalf
        # Setting last value to null and returning the had 
        if headFirstHalf is not None: 
            headFirstHalf.next = None
        return head  

        # Create a reverse helper method. 
        # 8 -> 10 -> 12 
    def reverse(self, head):
        prev = None 
        while head is not None: 
            next = head.next 
            head.next = prev 
            prev = head 
            head = next 
        return prev 