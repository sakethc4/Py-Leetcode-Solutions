from collections import defaultdict 
class Solution: # Ammortized it's O(M * N) Time & O(N) Space. 
    # We want to go through the list and return a list with each element 
    # being all the possible anagrams formed with those letters.  
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using a dictionary because I don't have to worry about default values. 
        output = collections.defaultdict(list)
        # Now we need to iterate thorugh the input list. 
        for string in strs:
            # We need to track the number of characters in our input. 
            charCounter = [0] * 26
            # Now we need to go through and count the characters of the given string. 
            for character in string: 
                # We need to map each character in our charCounter. 
                # The best way to do this would be to compare against a standardized value. 
                # So let's just use ascii values and compare against "a".
                charCounter[ord(character) - ord("a")] += 1
                # Now group all strings with similar count arrays together. 
            output[tuple(charCounter)].append(string)
        
        return output.values()

