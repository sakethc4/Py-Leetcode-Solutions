class Solution: # O(N) Time & O(1) Space. 
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        currentSum = nums[0]
        length = float('inf')
        while True: 
            # Shrinking the window. 
            if currentSum >= target: 
                length = min(length, right - left + 1)
                currentSum -= nums[left]
                left += 1
            else: 
                right += 1
                if right >= len(nums):
                    break 
                currentSum += nums[right] 
        return length if length != float('inf') else 0 