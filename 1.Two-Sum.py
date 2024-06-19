from typing import List
class Solution: # O(N) Time & O(N) Space. 
    # Goal is to return indices of the two nums that add up to the target
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Utilizing hashMap. 
        numbers = {} 
        # Iterate through our input array. 
        for index, number in enumerate(nums): 
            # Need to calculate how far off we are from out target. 
            difference = target - number 
            # Did we already store this value in our hashmap. 
            if difference in numbers: 
                # Found our sol. 
                return[numbers[difference], index] 
            else: 
                numbers[number] = index 
            

            