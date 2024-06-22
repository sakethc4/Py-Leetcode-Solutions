class Solution: # O(N) Time & O(N) Space. 
    def longestConsecutive(self, nums: List[int]) -> int:
        # We want to return the longest sequence we come across.
        longestSequence = 0 
        # Utilize a hashSet. 
        numSet = set(nums)
        # Iterate through our input. 
        for number in numSet:
            # Need to check if previous element is in our hashSet.
            if (number - 1) not in numSet: 
                length = 1
                # Otherwise we want to increment our longest sequence. 
                while (number + length) in numSet: 
                    length += 1 
                # Check the maximum sequence we hace came across. 
                longestSequence = max(longestSequence, length)
        # Return statement. 
        return longestSequence   


