class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        used = [False] * len(nums)
        curr = []

        def backtracking():
            if len(curr) == len(nums):
                result.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                used[i] = True
                curr.append(nums[i])
                backtracking()

                used[i] = False
                curr.pop()
        
        backtracking()
        return result
        