class Solution: # O(Log N) Time and O(1) Space.
    def find(self, num):
        # A number is a happy number if, after replacing it with a number equal to the sum of the square of all of its digits, leads us to a number 1. All other numbers will
        # never reach 1. Instead they will be stuck in a cycle of numbers that does not include 1. 
        # Okay so we can see that if we have a happy number we get to 1. If we don't it's and enless cycle of sums.
        # Similar to LL cycles. 
        # Initialize two pointers 
        slow, fast = num, num
        # Keep iterating through until we reach sum of 1, or we found an endless cycle. 
        while True: 
            # Let's have slow move by 1.
            slow = self.findSum(slow)
            # Fast can move by 2. 
            fast = self.findSum(self.findSum(fast))    
            # Condition for finding a cycle 
            if slow == fast: 
                break 
        return slow == 1 


    # Helper to find the sum of the squares 
    def findSum(self, num):
        sum = 0 
        # Iterate through input num
        while(num > 0):
            digit = num % 10 
            sum += digit * digit 
            num //= 10
        return sum 