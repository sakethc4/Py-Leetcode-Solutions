class Solution: # O(N) Time & O(1) Space. 
  def findMissingNumber(self, nums):
    index, length = 0, len(nums)
    while index < length:
      j = nums[index]
      if nums[index] < length and nums[j] != nums[index]:
        nums[index], nums[j] = nums[j], nums[index]
      else: 
        index += 1 
    # Iterate through the input array. 
    for index in range(len(nums)): 
      if nums[index] != index:
        return index 
    return length
