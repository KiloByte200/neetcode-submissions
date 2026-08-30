class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        
        def backtracking(index, remaining_target, current_combination):
            nonlocal result
            if index >= len(nums):
                return
            
            if remaining_target == 0:
                result.append(current_combination)
                return
            elif remaining_target < 0:
                return 
            
            backtracking(index,
                        remaining_target-nums[index],
                        current_combination + [nums[index]])

            backtracking(index + 1,
                        remaining_target,
                        current_combination)
        
        backtracking(0, target, [])
        return result
            
