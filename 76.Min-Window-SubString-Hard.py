class Solution: # O(N) Time & O(N) Space.
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        windowStart = 0
        for windowEnd in range(len(s)):
            c = s[windowEnd]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (windowEnd - windowStart + 1) < resLen:
                    res = [windowStart, windowEnd]
                    resLen = windowEnd - windowStart + 1
                window[s[windowStart]] -= 1
                if s[windowStart] in countT and window[s[windowStart]] < countT[s[windowStart]]:
                    have -= 1
                windowStart += 1
        windowStart, windowEnd = res
        return s[windowStart : windowEnd + 1] if resLen != float("infinity") else ""
