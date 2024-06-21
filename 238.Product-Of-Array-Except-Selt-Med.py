class Solution: # O(N) Time & O(N) Space.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # populate an array with 1 as the default value for an array of 
        # nums. 
        res = [1] * (len(nums))
        # We have a prefix value of 1, so we can multiply by whtvr 
        prefix = 1
        # Iterate through the list from beginning to calculate prefix sum. 
        for index in range(len(nums)):
            # set the value in the array to the prefex 
            res[index] = prefix 
            # Multiply by the current element to get the new prefix 
            prefix *= nums[index]
        postfix = 1
        # Iterate through the list from the end. 
        for index in range(len(nums) -1, -1, -1):
            # set the value in the array to the prefix value we have times 
            # the postfix value. 
            res[index] *= postfix
            # Multiply postfix by the current element to get the new postfix. 
            postfix *= nums[index]
        # Return the resulting list. 
        return res
