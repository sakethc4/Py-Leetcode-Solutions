from typing import List
class Solution: # O(N) Time & O(1) Space. 
    def maxProfit(self, prices: List[int]) -> int:
        # Validate the input. 
        if prices is None:
            return 0 
        # We need to to track the lowest price we come across.
        lowestPrice = prices[0]
        # Variable to track maximum profit
        maxProfit = 0 
        # Iterating through the prices input. 
        for price in prices: 
            # Find the new smallest price 
            lowestPrice = min(lowestPrice, price)
            # Need to handle finding the max profit 
            maxProfit = max(maxProfit, price - lowestPrice)
        # Return statement 
        return maxProfit 
