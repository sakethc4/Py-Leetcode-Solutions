from ast import List
class Solution: # O(N) Time and O(N) Space. 
    # Returning a boolean if any specific value appears at least twice. 
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Validate our input.
        if nums is None:
            return False 
        # Using a hashSet to keep track of characters we have already seen.
        seen = set() 
        # Iterate through our input. 
        for number in nums:
            if number in seen:
                return True 
            else:
                seen.add(number)
        # After iterating through the input nums, and we can't find a duplicate.
        return False 