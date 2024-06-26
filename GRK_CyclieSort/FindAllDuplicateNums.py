class Solution: # O(N) Time & O(1) Space. 
  def findNumbers(self, nums):
    index, duplicateNumbers = 0,[]
    while index < len(nums):
      j = nums[index] - 1  
      if nums[index] != nums[j]:
        nums[index], nums[j] = nums[j], nums[index]
      else: 
        index += 1 
    # Now determine duplicates. 
    for index in range(len(nums)):
      if nums[index] != index + 1:
        duplicateNumbers.append(nums[index])
    return duplicateNumbers
