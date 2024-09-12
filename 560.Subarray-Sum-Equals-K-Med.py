class Solution:
    # O(N) Time & O(N) Space. 
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Sample input: [1, 1, 1] 2
        # Output: 2 => [1, 1] & [1, 1]
        # Prefix_sum : [1, 2, 3]
        # Approach: Use hashMap to store all prefix_sums and their 
        # respective occurences we have seen so far. 
        # We can then see if the current prefix_sum - k in our hashMap.
        # If it is then we can return that value. 
        hash_map = {}
        # Handling edge case where the first element ends up being == k.
        hash_map[0] = 1
        count = 0 
        prefix_sum = 0
        for index in range(len(nums)):
            prefix_sum += nums[index]
            if prefix_sum - k in hash_map: 
                count += hash_map[prefix_sum - k]
            hash_map[prefix_sum] = 1 + hash_map.get(prefix_sum, 0)
        
        return count 

        
            
