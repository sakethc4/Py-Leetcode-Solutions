class Solution: # O(N)^3 Time and O(N) Space 
    def searchQuadruplets(self, arr, target):
        # Unique quadruple sum to target. 
        # Sort input array 
        arr.sort() 
        # Resulting quadruplets 
        results = [] 
        for index in range(len(arr) - 3):
            # Check to see if we reached same element & no out of bounds 
            if index > 0 and arr[index] == arr[index - 1]:
                continue
            # Find triplet 
            for indexTwo in range(len(arr) -2):
                # Same check as before 
                if indexTwo > index + 1 and arr[indexTwo] == arr[indexTwo - 1]:
                    continue 
                # Finding corresponding pair for those two elements 
                self.searchPairs(arr, target, index, indexTwo. results)

        return results

    def searchPairs(self, arr, target, first, second, results):
        left = second + 1
        right = len(arr) - 1 
        while(left < right):
            curr_sum = arr[first] + arr[second] + arr[left] + arr[right]
            if curr_sum == target:
                results.append([arr[first], arr[second], arr[left], arr[right]])
                left += 1 
                right -= 1 
                # Skipping repeating LHS elements 
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                # Skipping repeating RHS elements 
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
            elif curr_sum < target:
                left += 1 
            else:
                right -= 1 