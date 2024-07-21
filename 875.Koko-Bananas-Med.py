class Solution: # O(N Log N) Time & O(1) Space. 
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        least, most = 1, max(piles)
        result = most
        while least <= most: 
            k = least + (most - least) // 2 
            hours = 0 
            for pile in piles: 
                hours += math.ceil(pile / k)
            if hours <= h:
                result = min(result, k)
                most = k - 1 
            else: 
                least = k + 1 
        return result  
        # [3, 6, 7, 11]
        # least = 3, most = max(piles)
        # while least <= most: 
        # Track the eating rate(k) k = start + (end - start) // 2
        # track the hours. 
        # loop thru each pule and find how long it takes to eat with given k value. 
        # hours += math.ceil(pile / k)
        # if hours <= h update the result to the min(result, hours)
        # right = middle - 1
        # Otherwise we need a bigger value to finish the pile => start = middle + 1  