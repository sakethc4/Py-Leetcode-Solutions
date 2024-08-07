class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result, temporary = [], []
        counter = Counter(nums)
        # dfs function. 
        def dfs(nums, temporary, counter, result):
            # Base case. 
            if len(temporary) == len(nums):
                result.append(list(temporary))
                return 
            else: 
                for number in counter: 
                    if counter[number] == 0: 
                        continue 
                    temporary.append(number)
                    counter[number] -= 1 
                    dfs(nums, temporary, counter, result)
                    temporary.pop()
                    counter[number] += 1

        dfs(nums, temporary, counter, result)
        return result 