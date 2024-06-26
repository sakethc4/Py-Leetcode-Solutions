class Solution: # O(N) Time & O(1) Space. 
  def findNumber(self, nums):
    index, length = 0, len(nums)
    while index < length: 
      j = nums[index] - 1 
      if nums[index] > 0 and nums[index] <= length and nums[index] != nums[j]:
        nums[index], nums[j] = nums[j], nums[index]
      else: 
        index += 1 

    for index in range(length): 
      if nums[index] != index + 1: 
        return index + 1 
      
    return len(nums) + 1 
