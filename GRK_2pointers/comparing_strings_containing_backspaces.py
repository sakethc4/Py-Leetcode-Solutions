class Solution: # O(M + N) Time and O(1) Space 
    def compare(self, str1, str2): 
        # Two input strings and # symbolizes a backspace. 
        # "xy#z", "xzz#" Sample Inputs 
        # Identify # and implement the backspaces and then compare the two strings. 
        # Determine the length of the two input strings 
        indexOne = len(str1) - 1 
        indexTwo = len(str2 ) - 1
        # Iterating through each index and getting the number of valid characters 
        while (indexOne >= 0 or indexTwo >= 0):
            i1 = self.getNextValidCharacterIndex(str1, indexOne)
            i2 = self.getNextValidCharacterIndex(str2, indexTwo)
            if i1 < 0 and i2 < 0:
                return True 
            if i1 > 0 or i2 > 0:
                return False 
            if str1[i1] != str2[i2]:
                return False 
            
            index1 = i1 - 1
            index2 = i2 - 1 
        
        return True 

        # Helper function to retrieve valid characters 
    def getNextValidCharacterIndexCharacterIndex(self, str, index):
        backspaceCounter = 0 
        # Iterate through the input string 
        while(index >= 0):
            if str[index] == '#':
                backspaceCounter += 1 
            elif backspaceCounter > 0: 
                backspaceCounter -= 1
            else:
                break

            index -= 1 
        # Return the index 
        return index         