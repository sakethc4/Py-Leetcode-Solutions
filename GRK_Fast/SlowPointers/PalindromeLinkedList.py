class Solution: # O(N) Time and O(1) Space 
    def isPalindrome(self, head): 
        # Given: The head of a singly LL. Check if the list is a palindrome. 
        # Example input would be: 2 -> 4 -> 6 -> 4 -> 2 -> null. Observe that if you remove the middle value the first half is just the reverse of second half. 
        # First things first lets handle head or head.next being null. Return True. 
        if head is None or head.next is None: 
            return True 
        # Find the middle value. 
        # Initialize two pointers. 
        slow, fast = head, head 
        # Iterating throgh Linked List. 
        while (fast is not None and fast.next is not None): 
            # Move slow by 1. 
            slow = slow.next
            # Move fast by 2. 
            fast = fast.next 
        # Now we have a middle point we can go ahead and reverse the second half of the LL. 
        headSecondHalf = self.reverse(slow)
        # We also need to store the reversed part that way we can redo it later. 
        copyOfHeadSecondHalf = headSecondHalf
        # Compare the two halves.
        while (head is not None and headSecondHalf is not None):
            if head.val != headSecondHalf.val:
                break
            # Move the two heads. 
            head = head.next 
            headSecondHalf = headSecondHalf.next 
        # After compairson fix the LL not sure if needed but just doing it anyway. 
        self.reverse(copyOfHeadSecondHalf)
        # Check to see if the head values match 
        if head is None or headSecondHalf is None:
            return True 
        
        return False 
    
    # Aux method reverse. 
    # 6 -> 4 -> 2 
    def reverse(self, head):
        prev = None 
        while (head is not None):
            next = head.next 
            head.next = prev 
            prev = head 
            head = next
        return prev 
