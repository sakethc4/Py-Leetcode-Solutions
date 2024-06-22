class Solution: # O(N) Time & O(1) Space. 
  def sort(self, nums):
    # Track index. 
    index = 0 
    # Iterate through input array. 
    while index < len(nums):
      # We need to calculate where the number should be placed. 
      placement = nums[index] - 1
      # Now we need to determine with the element in that position right now. 
      if nums[index] != nums[placement]:
        # Swap.
        nums[index], nums[placement] = nums[placement], nums[index]
      else: 
        # Element placement is valid. 
        index += 1 
    return nums
