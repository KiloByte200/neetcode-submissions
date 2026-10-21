class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        best_at_i = nums[0]
        best_so_far = nums[0]

        for i in range(1, len(nums)):

            best_at_i = max(best_at_i + nums[i], nums[i])
            best_so_far = max(best_at_i, best_so_far)
        
        return best_so_far
        