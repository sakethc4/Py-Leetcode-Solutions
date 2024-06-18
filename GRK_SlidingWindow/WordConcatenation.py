class Solution: # O(N) Ammortized Time & O(M) Space Ammortized. Where N is input str1 and M is the input words (and words associated). 
    def findWordConcatenation(self, str1, words):
        if len(words) == 0 or len(words[0]) == 0:
            return []

        wordFrequency = {}

        for word in words:
            if word not in wordFrequency:
                wordFrequency[word] = 0
            wordFrequency[word] += 1

        results = []
        wordCount = len(words)
        wordLetters = len(words[0])

        for i in range((len(str1) - wordCount * wordLetters)+1):
            seen = {}
            for j in range(0, wordCount):
                nextIndex = i + j * wordLetters
                # Get the next word from the string.
                word = str1[nextIndex: nextIndex + wordLetters]
                if word not in wordFrequency:  
                    break

                # Add the word to the seen map.
                if word not in seen:
                    seen[word] = 0
                seen[word] += 1

                if seen[word] > wordFrequency.get(word, 0):
                    break

                if j + 1 == wordCount: 
                    results.append(i)

        return results