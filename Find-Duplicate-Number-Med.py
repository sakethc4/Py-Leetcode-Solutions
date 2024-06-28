class Solution: # O(N) Time & O(1) Space.
    # Sample in: [1,3,4,2,2]
    def findDuplicate(self, nums: List[int]) -> int:
        # Initialize two pointers. 
        slow, fast = nums[0], nums[0]
        while True: 
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break 
        # Now that we have found our cycle. 
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow 