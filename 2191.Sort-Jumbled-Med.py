class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []
        
        for index, number in enumerate(nums):
            number = str(number)
            mapN = 0
            for char in number:
                mapN *= 10  
                mapN += mapping[int(char)]

            pairs.append((mapN, index))

        pairs.sort()
        return [nums[p[1]] for p in pairs]