class Solution: # O(N)^2 Time & O(1) Space. 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # in place sorting is n log n time 
        triplets = []
        # Go thru each index in nums list 
        for index in range(len(nums)):
            # If we come across an identical value then we skip so we dont get an
            # identical threeSum.  
            if index > 0 and nums[index] == nums[index - 1]: 
                continue 
            # Find the pair that goes with the index. 
            self.findPairs(nums, -nums[index], index + 1, triplets) 
        # return triplets. 
        return triplets 

    def findPairs(self, nums, target, left, triplets): 
        # define right pointer 
        right = len(nums) - 1 
        # Go thru until right before the pointers cross. 
        while left < right: 
            # Curr_sum tracks the total sum at the pointers. 
            curr_sum = nums[left] + nums[right] 
            # If we reach target 
            if curr_sum == target: 
                # append the three values. 
                triplets.append([-target, nums[left], nums[right]]) 
                # Move to the next left p 
                left += 1 
                # Move to the right p 
                right -= 1 
                # While not crossing pointers check to see if 
                # two number are the same to ensure no duplicate triplets
                while left < right and nums[left] == nums[left - 1]: 
                    left += 1 
                # While not crossing check right pointers to ensure 
                # no duplicate triplets. 
                while left < right and nums[right] == nums[right + 1]: 
                    right -= 1 
            elif target > curr_sum: 
                left += 1 
            else: 
                right -= 1 
            
        # [-1, 0, 1, 2, -1, -4] 
