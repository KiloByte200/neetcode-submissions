class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr_subset = []

        def backtracking(index: int):
            if len(nums) == index:
                result.append(curr_subset.copy())
                return
            
            # inclusive
            curr_subset.append(nums[index])
            backtracking(index+1)

            curr_subset.pop()

            #exclusive
            backtracking(index+1)

        backtracking(0)
        return result