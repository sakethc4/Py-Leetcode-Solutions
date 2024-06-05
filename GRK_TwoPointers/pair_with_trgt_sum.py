class Solution: 
    # Searching for target pairs can do this in O(n) with one loop 
    def search(self, arr, target_sum):
        # Create a left and right pointer 
        left, right = 0, len(arr) - 1 
        # Iterate through the array, while our two pointers don't cross
        while left < right: 
            curr_sum = arr[left] + arr[right]
            # we found our target_sum
            if curr_sum == target_sum:
                return [left,right]
            # current sum too small so we move to the left. 
            elif curr_sum < target_sum:
                left += 1
            # Otherwise current sum to big so we move to the right 
            else:
                right -= 1 
        # The target sum couldn't be found so just return an arbitrary value. 
        return[-1,-1]
                
