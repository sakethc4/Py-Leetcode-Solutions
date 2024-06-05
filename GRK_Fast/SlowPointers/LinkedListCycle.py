class Solution:
    def hasCycle(self, head): # O(N) Time and O(1) Space 
        # Okay so if a LinkedList has a cycle then the slow pointer should be able to in theory 
        # catch the fast pointer 
        # Initializing a slow and fast pointer to start at the head pointer  
        slow, fast = head 
        # Iterate through the linked list while the fast pointer does not reach a null value 
        while fast is not None and fast.next is not None:
            # Let's move the fast pointer by 2 and the slow pointer by one each iteration
            fast = fast.next.next
            slow = slow.next
            # If the two ever meet then we know it has a cycle 
            if slow == fast:
                return True 
        # Otherwise return false because it's not a cyclic LinkedList. 
        return False
