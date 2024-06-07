class Solution: # O(N) Time and O(1) Space 
    def findCycleStart(self, head): 
        # Given the head of a LL we want to find where the cycle starts. 
        # Sample input: 1 => 2=> 3 => 4 => 5 => 6=> 3 (cycle starts at 3)
        # Tracing input                 
        # Sol. We want a fast and slow pointer and we need to determine where the 
        # cycle starts the first sol that comes to mind is that we figure out where
        # the cycle starts if we figure out where the two pointers meet one another. 
        # They should meet where the cycle starts, so we need to determine the meeting point.
        # After moving slow back to head and moving both at a constant rate. 
        # ----
        # Check to validate input head 
        if head == None or head.next == None:
            return None 
        # Initialize our slow and fast moving pointers 
        slow, fast = head, head 
        # Iterate through input LL 
        while fast is not None and fast.next is not None: 
            # Moving the pointers as needed 
            slow = slow.next 
            fast = fast.next.next 
            # If the two meet we have found the starting point of our cycle. 
            if slow == fast:  
                # We can set out slow pointer to head 
                slow = head 
                while slow != fast: 
                    slow = slow.next 
                    fast = fast.next 
                return slow 
        return None 
