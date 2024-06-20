class NumArray: # O(N) Time and O(N) Space. 

    def __init__(self, nums: List[int]):
        # initialize a prefix array  
        self.prefix = [] 
        # total counter
        total = 0 
        # Iterate through the input list. 
        for number in nums: 
            total += number 
            self.prefix.append(total)



    def sumRange(self, left: int, right: int) -> int:
        preRight = self.prefix[right]
        if left > 0:
            preLeft = self.prefix[left - 1]
        else: 
            preLeft = 0
        return(preRight - preLeft)
