class Solution: # O(N) Time & O(N) Space. 
    # We want to get the k most frequent elements, so whatever elements 
    # in the list match the frequency of the k integer parameter. 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We can utilize a hashMap to map occurences. 
        count = {} 
        # We also need to keep track of all the nums in our list. 
        frequency = [[] for index in range(len(nums) + 1)]
        # List to hold output.
        results = []  
        # Iterate through each number. Adding it to our hashMap. 
        for number in nums: 
            count[number] = 1 + count.get(number, 0)
        # Iterate through hashMap adding the number of items 
        # to the corresponding bucket. 
        for number, count in count.items():
            frequency[count].append(number)
        # Iterate through frequency and determine the k most frequent 
        # elements. Start at end of array. Move till 0 decrementing 
        # by -1 each time. 
        for index in range(len(frequency) - 1, 0, -1):
            for number in frequency[index]:
                results.append(number)
                # If we reach k elements in results. 
                if len(results) == k: 
                    return results 

        