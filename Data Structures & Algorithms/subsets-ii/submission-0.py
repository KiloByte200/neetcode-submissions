class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]
        curr = []

        def backtracking(start: int)-> None:
            if start >= len(nums):
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                curr.append(nums[i])
                result.append(curr.copy())

                backtracking(i+1)
                curr.pop()

        backtracking(0)
        return result