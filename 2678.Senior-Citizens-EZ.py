class Solution: # O(N) Time & O(1) Space. 
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for detail in details:
            print(detail[13:])
            if int(detail[11:13]) > 60:
                count += 1 
        return count 
