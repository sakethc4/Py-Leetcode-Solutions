class Solution: # O(N) Time & O(N) Space. 
    def nextGreaterElement(self, nums1, nums2):
        stack, hashMap = [], {} 
        # Iterate through input pairs (nums2).
        for num in nums2: 
            while stack and stack[-1] < num:
                hashMap[stack.pop()] = num 
            stack.append(num)

        # return the hashMap with numbers mapped accordingly. 
        return[hashMap.get(num, -1) for num in nums1]

