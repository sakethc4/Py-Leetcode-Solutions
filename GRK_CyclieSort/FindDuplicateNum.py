class Solution: # O(N) Time & O(1) Space. 
  def findNumber(self, nums):
    # Store the length of the input. 
    index, length = 0, len(nums)
    while index < length: 
      if nums[index] != index + 1:
        j = nums[index] - 1 
        if nums[index] != nums[j]:
          nums[index], nums[j] = nums[j], nums[index]
        else: 
          return nums[index]
      else:
        index += 1 
    return -1
