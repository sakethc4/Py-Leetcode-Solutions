class Solution: # O(NLogN) Time & O(N) Space. 
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        for index in sorted(range(len(positions)), key = lambda index: positions[index]):
            if directions[index] == 'R':
                stack.append(index)
            else:
                while stack and healths[stack[-1]] < healths[index]:
                    healths[index] -= 1
                    healths[stack.pop()] = 0
                if stack:
                    if healths[stack[-1]] == healths[index]:
                        healths[stack.pop()] = 0
                    else:
                        healths[stack[-1]] -= 1
                    healths[index] = 0
        return [health for health in healths if health] 