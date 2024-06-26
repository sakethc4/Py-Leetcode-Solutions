class Solution: # O(N) Time & O(N) Space (It would be O(1) if we ignore output array).
  def findNumbers(self, nums):
    length, missingNumbers = 0, []
    index = 0 
    while index < len(nums):
      j = nums[index] - 1
      # Check to see if it's in the right spot. 
      if nums[j] != nums[index]: 
        nums[index], nums[j] = nums[j], nums[index]
      else: 
        index += 1 
    # Now find out of place elements. 
    for index in range(len(nums)):
      if nums[index] != index + 1:
        missingNumbers.append(index + 1)  
        
    
    return missingNumbers
