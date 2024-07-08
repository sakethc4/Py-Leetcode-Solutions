class Solution: # O(N) Time & O(1) Space. 
    def commonChars(self, words: List[str]) -> List[str]:
        totalCount = Counter(words[0])
        for word in words[1:]:
            wordCount = Counter(word)
            for char in totalCount: 
                totalCount[char] = min(totalCount[char], wordCount[char])
        result = []
        for char, freq in totalCount.items():
            result.extend([char] * freq)
        return result 
